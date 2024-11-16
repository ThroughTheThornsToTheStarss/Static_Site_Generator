import unittest
from markdown_to_blocks import * 
from htmlnode import *

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks_1(self):
        text = """# Heading\n\nParagraph here\nwith multiple lines\n\n* List item 1\n* List item 2\n"""
        a=markdown_to_blocks(text)
        b = [
            "# Heading","Paragraph here\nwith multiple lines","* List item 1\n* List item 2"
        ]
        self.assertEqual(b,a)
    
    def test_markdown_to_blocks_2(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        a=markdown_to_blocks(text)
        b = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(b,a)

    def test_block_to_block_type_heading(self):
        text1 = "# Hi"
        text2 = "##### This is first tack"
        self.assertEqual(block_to_block_type(text1), "heading")
        self.assertEqual(block_to_block_type(text2), "heading")
         
    def test_block_to_block_type_code(self):
        text = "```print()```"
        self.assertEqual(block_to_block_type(text), "code")

    def test_block_to_block_type_quote(self):
        text = "> line 1\n> line 2\n> line 3"
        self.assertEqual(block_to_block_type(text), "quote")

    def test_block_to_block_type_unordered_list(self):
        text = "* line 1\n- line 2\n* line 3"
        self.assertEqual(block_to_block_type(text), "unordered_list")
     
    def test_block_to_block_type_ordered_list(self):
        text = "1. line 1\n2. line 2\n3. line 3"
        self.assertEqual(block_to_block_type(text), "ordered_list")

    def test_block_to_block_type_paragraph(self):
        text = "1. line 1\n line 2\n* line 3"
        self.assertEqual(block_to_block_type(text), "paragraph")

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), "heading")
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "code")
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), "quote")
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), "unordered_list")
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), "ordered_list")
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")
    
    
    def test_markdown_to_html_node(self):
        text = """# Header

This is a *paragraph*

* List item 1
* List item 2"""
        result = markdown_to_html_node(text)
        html = result.to_html()
       
        predict = "<div><h1>Header</h1><p>This is a <i>paragraph</i></p><ul><li>List item 1</li><li>List item 2</li></ul></div>"
      
        self.assertEqual(html, predict)

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""
        result = markdown_to_html_node(md)
        html = result.to_html()
        predict = "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>"
        self.assertEqual(html, predict)


    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

