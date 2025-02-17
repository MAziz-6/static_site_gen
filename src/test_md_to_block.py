import unittest
from md_to_block import markdown_to_blocks

class TestMDtoBlocks(unittest.TestCase):
    def test_header(self):
        markdown = """
            # This is a header

            """
        node = markdown_to_blocks(markdown)
        print("test node:", node)
        expected = ["# This is a header"]
        self.assertEqual(node, expected)

    def test_header_and_paragraph(self):
        markdown = """
            # This is a header

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            """
        node = markdown_to_blocks(markdown)
        print("test node:", node)
        expected = [
            "# This is a header", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
            ]
        self.assertEqual(node, expected)

    def test_header_paragraph_and_bullets(self):
        markdown = """
            # This is a header

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item

            """
        node = markdown_to_blocks(markdown)
        print("test node:", node)
        expected = [
            "# This is a header", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(node, expected)