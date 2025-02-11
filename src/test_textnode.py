import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node1 = TextNode("This is a Link node", TextType.LINKS, "WEBSITE.COM")
        node2 = TextNode("This is a Link node", TextType.BOLD, "WEBSITE.COM")
        self.assertNotEqual(node1, node2)

    def test_repr_url_behavior(self):
        # Type: LINKS with URL should give URL in output of repr
        link_node = TextNode("Check this link", TextType.LINKS, "example.com")
        self.assertIn("example.com", repr(link_node), "URL should appear for LINKS type")

        # Type not LINKS should not give URl
        non_link_node = TextNode("No Link here", TextType.TEXT, "example.com")
        self.assertNotIn("example.com", repr(non_link_node), "URL should not appear for Non-LINKS types")

        empty_url_node = TextNode("Broken link", TextType.LINKS)
        self.assertNotIn("http", repr(empty_url_node), "Even when Links type, empty url input should stay empty")

    def test_empty_url_with_links(self):
        w_url_node = TextNode("Is there a URL?", TextType.LINKS, "website.com")
        wo_url_node = TextNode("Is there a URL?", TextType.LINKS)
        self.assertNotEqual(w_url_node, wo_url_node)
        
    def test_none_v_missing_url(self):
        none_url_node = TextNode("Should be nutttin to see here", TextType.LINKS, None)
        missing_url_node = TextNode("Should be nutttin to see here", TextType.LINKS)
        self.assertEqual(none_url_node, missing_url_node, "Even with LINKS, none or missing url should not populate")

if __name__ == "__main__":
    unittest.main()