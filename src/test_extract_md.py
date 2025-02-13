import unittest
from extract_md import extract_markdown_images, extract_markdown_links

class TestExtractMd(unittest.TestCase):
    def test_img_base(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(node, expected)

    def test_img_none_text(self):
        with self.assertRaises(ValueError):
            extract_markdown_images(text=None)

    def test_img_blank_text(self):
        node = extract_markdown_images(text="No image here")
        expected = []
        self.assertEqual(node, expected)

    def test_img_mixed_content(self):
        text = "Here's an ![image](url1) and a [link](url2)"
        node = extract_markdown_images(text)
        expected = [("image", "url1")]
        self.assertEqual(node, expected)

    def test_link_base(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(node, expected)

    def test_link_none_text(self):
        with self.assertRaises(ValueError):
            extract_markdown_links(text=None)

    def test_link_blank_text(self):
        node = extract_markdown_links("No links here")
        expected = []
        self.assertEqual(node, expected)

    def test_link_mixed_content(self):
        text = "Here's an ![image](url1) and a [link](url2)"
        node = extract_markdown_links(text)
        expected = [("link", "url2")]
        self.assertEqual(node, expected)