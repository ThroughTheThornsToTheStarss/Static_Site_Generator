import re, os
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from htmlnode import *

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type_block = block_to_block_type(block)
        if type_block == "heading":
            hashes = re.findall(r"#", block)
            count = len(hashes)
            if count == 1:
                content = (block[(count+1):])
                return content.strip()
            
    raise Exception("missing heading")    


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, encoding="utf-8") as f:
        markdown_content = f.read()
    with open(template_path, encoding="utf-8") as f:    
        pattern_content = f.read()
    html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    pattern_content = pattern_content.replace("{{ Title }}", title)
    pattern_content = pattern_content.replace("{{ Content }}", html)
    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(pattern_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        full_path_copy = os.path.join(dir_path_content, file)
        if os.path.isfile(full_path_copy):
            dest_path = os.path.relpath(full_path_copy, dir_path_content)
            if dest_path.endswith(".md"):
                dest_path =re.sub(r'.md\b','.html',dest_path)
                dest_dir = os.path.join(dest_dir_path, dest_path) 
                generate_page(full_path_copy, template_path, dest_dir)
        else:
            dest_path = os.path.relpath(full_path_copy, dir_path_content)
            dest_dir = os.path.join(dest_dir_path, dest_path) 
            generate_pages_recursive(full_path_copy, template_path, dest_dir )
    