import unittest
from block_types import block_to_block_type

class TestBlockTypeSelection(unittest.TestCase):
    def test_header_proper(self):
        block = "# header"
        node = block_to_block_type(block)
        expected = "heading"
        self.assertEqual(node, expected)
    def test_header_improper(self):
        block = "######## header"
        node = block_to_block_type(block)
        expected = "heading"
        self.assertNotEqual(node, expected)
    def test_quote(self):
        block = """
        > this is a quote
        > so is this
        """
        node = block_to_block_type(block)
        expected = "quote"
        self.assertEqual(node, expected)
    def test_unordered_list(self):
        pass
    def test_ordered_list(self):
        pass
    def test_code_block(self):
        pass