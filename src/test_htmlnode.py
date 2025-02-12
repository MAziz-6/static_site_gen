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

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        # baseline: a few leafnodes in callout
        n_baseline = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(n_baseline.to_html(), expected)
        
        # c1: nested parent nodes
        nested = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        n_parent_nested = ParentNode(
            "p",
            [nested],
        )
        expected = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
        self.assertEqual(n_parent_nested.to_html(), expected)

        # c2: mix of leaf nodes and parent nodes
        n_mixed = ParentNode(
            "p",
            [
                nested,
                LeafNode("b", "Bold Test"),
            ],
        )
        expected = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold Test</b></p>"
        self.assertEqual(n_mixed.to_html(), expected)
        
        # c3: empty children list
        n_empty_children = ParentNode(
            "p",
            [],
        )
        expected = "<p></p>"
        self.assertEqual(n_empty_children.to_html(), expected)

        # c4: None children callout
        n_none_children = ParentNode("p", children=None)
        with self.assertRaises(ValueError):
            n_none_children.to_html()

        # c5: Props added
        n_props = ParentNode(
            "p",
            [],
            {"href": "https://www.google.com"},
        )
        expected = '<p href="https://www.google.com"></p>'
        self.assertEqual(n_props.to_html(), expected)

        # c6: tag is None
        n_none_tag = ParentNode(tag=None, children=[])
        with self.assertRaises(ValueError):
            n_none_tag.to_html()

        # c7: multi props 
        n_mprops = ParentNode(
            "p",
            [],
            {
               "href": "https://www.google.com",
               "id": "main"
            }
        )
        expected = '<p href="https://www.google.com" id="main"></p>'
        self.assertEqual(n_mprops.to_html(), expected)

        # c8: props on multiple levels of nested nodes
        n_nested_props = ParentNode(
            "p",
            [
                LeafNode("a", "we got one", {"href": "https://www.google.com"}),
                LeafNode("b", "Bold Test")
            ],
            {
                "id": "main",
                "data": "test_data"
            }
        )
        expected = '<p id="main" data="test_data"><a href="https://www.google.com">we got one</a><b>Bold Test</b></p>'
        self.assertEqual(n_nested_props.to_html(), expected)

if __name__ == "__main__":
    unittest.main()