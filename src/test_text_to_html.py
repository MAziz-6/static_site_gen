import unittest
from text_to_html import *
from textnode import TextNode


class TestTexttoHTML(unittest.TestCase):
    def test_text_node_to_html_node(self):
        # Basic text Test
        node = TextNode("Hello", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello")

        # Bold
        node = TextNode("Hello", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Hello")

        # Italic
        node = TextNode("Hello", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Hello")

        # Code
        node = TextNode("Hello", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Hello")

        # Link
        node = TextNode("Hello", TextType.LINK, url="example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Hello")
        self.assertEqual(html_node.props["href"], "example.com")
        
        # Image
        node = TextNode("Hello", TextType.IMAGE, url="example.com", alt="alt")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "example.com")      
        self.assertEqual(html_node.props["alt"], "alt") 

        # Incorrect text type
        node = TextNode("Hello", "not_a_text_type")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()