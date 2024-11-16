import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("wrong input")
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
               split_nodes.append(TextNode(split_node[i],TextType.TEXT))
            else:
              split_nodes.append(TextNode(split_node[i],text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
      return re.findall(r"(?<=!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
      return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)




def split_nodes_link(old_nodes):
    
    
    new_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_node.append(node)
            continue
        
        list_pat = []
        remaining_text = node.text
        all_patterns = extract_markdown_links(node.text)
        if len(all_patterns) == 0:
            new_node.append(node)
            continue
        
        for pattern in all_patterns:
            link, url = pattern
            pattern_li = f"[{link}]({url})"
            el, remaining_text = remaining_text.split(pattern_li, 1 )
        
            if el:
                list_pat.append(TextNode(el, TextType.TEXT))

            list_pat.append(TextNode(link,TextType.LINK, url))
            
        if remaining_text:
            list_pat.append(TextNode(remaining_text, TextType.TEXT))
        new_node.extend(list_pat)
    return new_node

def split_nodes_image(old_nodes):
    
    
    new_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_node.append(node)
            continue
        list_pat = []
        remaining_text = node.text
        all_patterns = extract_markdown_images(node.text)
        if len(all_patterns) ==0:
            new_node.append(node)
            continue
        for pattern in all_patterns:
            image, url = pattern
            pattern_im = f"![{image}]({url})"
            el, remaining_text = remaining_text.split(pattern_im, 1 )
        
            if el:
                list_pat.append(TextNode(el, TextType.TEXT))

            list_pat.append(TextNode(image,TextType.IMAGE, url))
            
        if remaining_text:
            list_pat.append(TextNode(remaining_text, TextType.TEXT))
        new_node.extend(list_pat)
    return new_node




def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(nodes,"`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes,"**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    
    return nodes


