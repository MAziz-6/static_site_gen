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

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        # case 1: leaf node with a tag and value
        node1 = LeafNode(tag="p", value="Here is some text")
        expect1 = "<p>Here is some text</p>"
        self.assertEqual(node1.to_html(), expect1)

        # case 2: leaf node with none tag, but with value
        node2 = LeafNode(tag=None, value="Here is some text")
        expect2 = "Here is some text"
        self.assertEqual(node2.to_html(), expect2)
        
        # case 3: leaf node with no value
        node3 = LeafNode(tag="a", value=None)
        with self.assertRaises(ValueError):
            node3.to_html()

        # case 4: leaf node with props handling
        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expect4 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node4.to_html(), expect4)