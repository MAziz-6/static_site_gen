import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(props={"href":"https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode(tag="p", value="value", children=['child1', 'child2'],props=None)
        expected = f"tag:p, value:value, children:['child1', 'child2'], props:{None}"
        self.assertEqual(repr(node), expected)