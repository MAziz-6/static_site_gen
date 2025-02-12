import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter

"""
This Input:
node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

Gives this Output:
[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
]
"""

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