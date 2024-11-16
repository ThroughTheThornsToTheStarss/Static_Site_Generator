import re
from htmlnode import *
from textnode import text_node_to_html_node
from split_delimiter import text_to_textnodes

def markdown_to_blocks(markdown):
        clean_block = []
        blocks = markdown.split("\n\n")
        for block in blocks:
            stripped = block.strip()
            if stripped:
                clean_block.append(stripped)
        return clean_block

def block_to_block_type(block):
        lines = block.split("\n")

        if re.match(r"^#{1,6}\s", lines[0]):
            return "heading"
        elif re.match(r"^`{3}(.*?)`{3}$", block, re.DOTALL):
            return "code"
        elif all(re.match(r"^>\s", line) for line in lines):
            return "quote"
        elif all(re.match(r"^\*\s|^-\s", line) for line in lines): 
            return "unordered_list"
        for i, line in enumerate(lines):
            match = re.match(r"(\d+)\.\s", line)
            if not match:
                return "paragraph"
            number = int(match.group(1))
            if i+1 != number:
                return "paragraph"
        return "ordered_list"


def markdown_to_html_node(markdown):
        markdown_blocks = markdown_to_blocks(markdown)
        list_blocks = []
        for block in markdown_blocks:
            type_block = block_to_block_type(block)
            if type_block == "quote":
                list_blocks.append(markdown_to_html_node_quote(block))
            elif type_block == "heading":
                list_blocks.append(markdown_to_html_node_heading(block))
            elif type_block == "code":
                 list_blocks.append(markdown_to_html_node_code(block))
            elif type_block == "unordered_list":
                 list_blocks.append(markdown_to_html_node_unordered_list(block))
            elif type_block == "ordered_list":
                 list_blocks.append(markdown_to_html_node_ordered_list(block))
            elif type_block == "paragraph":
                 list_blocks.append(markdown_to_html_node_paragraph(block))   

        return ParentNode(tag = "div", children = list_blocks)

def  markdown_to_html_node_quote(block):
        list_nodes = []
     
        clean_block = re.sub(r"^>\s", "", block)
       
        lines = clean_block.split("\n")
        
        for line in lines:
            if line:
                line = re.sub(r"^>\s", " ", line)
                list_nodes.extend(text_to_children(line))

        return  ParentNode(tag="blockquote", children=list_nodes)




def  markdown_to_html_node_heading(block):
            hashes = re.findall(r"#", block)
            count = len(hashes)
            content = block[(count+1):]
            return (ParentNode(tag = f"h{count}", children=text_to_children(content.strip())))
        


def markdown_to_html_node_code(block):
        
        clean_block = re.sub(r"```","", block)  
        
        code_node = LeafNode(tag = "code", value = clean_block.strip())
        return ParentNode(tag = "pre", children=[code_node])

def markdown_to_html_node_unordered_list(block): 
    list_heading = []
    
    lines = block.split("\n")
    for line in lines:
      clean_line = re.sub(r"^\*\s|^-\s","", line)
      if clean_line.strip():
        line_childe = text_to_children(clean_line)
        list_heading.append(ParentNode(tag = "li", children=line_childe))
    return ParentNode(tag = "ul", children=list_heading)  

def markdown_to_html_node_ordered_list(block):
    
    list_heading = []
    
    lines = block.split("\n")
    for line in lines:
      clean_line = re.sub(r"\d+\.\s","", line)
      if clean_line.strip():
        line_childe = text_to_children(clean_line)
        list_heading.append(ParentNode(tag = "li", children=line_childe))
    return ParentNode(tag = "ol", children=list_heading)  
   


def markdown_to_html_node_paragraph(block):
    a = block.split("\n")
    b = " ".join(a)   
    return  ParentNode(tag = "p", children= text_to_children(b))

def text_to_children(text):
    leaf_node = []
    level_1 = text_to_textnodes(text)
    for el in level_1:
        leaf_node.append(text_node_to_html_node(el))
    return leaf_node