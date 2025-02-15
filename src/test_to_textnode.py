import unittest
from to_textnode import text_to_textnodes
from textnode import TextNode, TextType

class TestToTextNode(unittest.TestCase):
    def test_baseline(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        node = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ]
        self.assertEqual(node, expected)

    def test_empty_text(self):
        text = ""
        node = text_to_textnodes(text)
        expected = [TextNode("", TextType.TEXT)]
        self.assertEqual(node, expected)

    def test_one_type_of_md(self):
        text = "This is **bold**"
        node = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("", TextType.TEXT)
        ]
        self.assertEqual(node, expected)

    def test_nested_md(self):
        text = "Here is **nested *markdown* boy**"
        node = text_to_textnodes(text)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("nested ", TextType.BOLD),
            TextNode("markdown", TextType.ITALIC),
            TextNode(" boy", TextType.BOLD),
            TextNode("", TextType.TEXT)
        ]
        self.assertEqual(node, expected)