import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter


class Test_Split_Nodes(unittest.TestCase):
    def test_baseline(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_delim(self): 
        node = TextNode("This is plain text without code", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is plain text without code", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)

    def test_multiple_of_same_delim(self):
        node = TextNode("`code1` and `code2`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("",TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_unmatched_delim(self):
        node = TextNode("This is `unfinished code", TextType.TEXT)
        with self.assertRaises(ValueError):  
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_text_type(self):
        node = TextNode("This is bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is bold", TextType.BOLD)]  
        self.assertEqual(new_nodes, expected)