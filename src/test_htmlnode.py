import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):


    def test_HTMLNode1(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
    
    def test_HTMLNode2(self):
        node = HTMLNode(props={"href": "https://www.google.com", "doc" : "www.doc.com"})
        self.assertIn( ' href="https://www.google.com"', node.props_to_html())
        self.assertIn( ' doc="www.doc.com"', node.props_to_html())

    def test_HTMLNode3(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), '')
    
    def test_HTMLNode4(self):
        node= HTMLNode(props={"href": "https://www.google.com", "doc" : "www.doc.com"})
        result = node.props_to_html()
        self.assertEqual(result.count(" "), 2 )





    def test_LeafNode1(self):
        leafnode = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leafnode.to_html(), '<p>This is a paragraph of text.</p>')
        
    def test_LeafNode2(self):
        leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leafnode.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_value_error_LeafNode(self):
        leafnode = LeafNode("a",None, {'href": "https://www.google.com'})
        with self.assertRaises(ValueError):
            leafnode.to_html()




    def test_to_html_with_children(self):
        parent_node_test = ParentNode(
         "p",
          [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
          ],
        )

        self.assertEqual(parent_node_test.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_many_children(self):
        childe_in = LeafNode("p", "This is a paragraph of text.")
        childe = ParentNode("p", [childe_in])
        parent = ParentNode("a", [childe])
        self.assertEqual(parent.to_html(), "<a><p><p>This is a paragraph of text.</p></p></a>")




















if __name__ == "__main__" :
    unittest.main()