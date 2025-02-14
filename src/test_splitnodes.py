import unittest
from textnode import TextNode, TextType
from splitnodes import *


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

class Test_Split_Nodes_Link(unittest.TestCase):
    def test_no_links(self):
        input_nodes = [TextNode("This is plain text.", TextType.TEXT)]
        expected = [TextNode("This is plain text.", TextType.TEXT)]
        result = split_nodes_link(input_nodes)
        self.assertEqual(result, expected)

    def test_single_link(self):
        input_nodes = [TextNode("Visit [Boot.dev](https://www.boot.dev).", TextType.TEXT)]
        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(".", TextType.TEXT)
        ]
        result = split_nodes_link(input_nodes)
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        input_nodes = [TextNode("Links: [One](https://link1.com) and [Two](https://link2.com).", TextType.TEXT)]
        expected = [
            TextNode("Links: ", TextType.TEXT),
            TextNode("One", TextType.LINK, "https://link1.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Two", TextType.LINK, "https://link2.com"),
            TextNode(".", TextType.TEXT)
        ]
        result = split_nodes_link(input_nodes)
        self.assertEqual(result, expected)

    def test_empty_text(self):
        input_nodes = [TextNode("", TextType.TEXT)]
        expected = [TextNode("", TextType.TEXT)]
        result = split_nodes_link(input_nodes)
        self.assertEqual(result, expected)

    def test_adjacent_links(self):
        input_nodes = [TextNode("[One](https://link1.com)[Two](https://link2.com)", TextType.TEXT)]
        expected = [
            TextNode("One", TextType.LINK, "https://link1.com"),
            TextNode("Two", TextType.LINK, "https://link2.com"),
        ]
        result = split_nodes_link(input_nodes)
        self.assertEqual(result,expected)