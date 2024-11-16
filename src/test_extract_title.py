import unittest
from extract_title import extract_title
class TestTitle(unittest.TestCase):

    def test_h1_heading(self):
        markdown = "# Hello World"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")

    def test_missing_h1(self):
        markdown = "## No h1 here"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("missing heading" in str(context.exception))

        
    def test_extact_title(self):
        markdown = """
# this is an h1

this is paragraph text

## this is an h2
"""
        content = extract_title(markdown)
        self.assertEqual(content, "this is an h1")

if __name__ == '__main__':
    unittest.main()