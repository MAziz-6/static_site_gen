import unittest
from block_types import block_to_block_type, BlockType

class TestBlockTypeSelection(unittest.TestCase):
    def test_header_proper(self):
        block = "# header"
        node = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertEqual(node, expected)

    def test_header_improper(self):
        block = "######## header"
        node = block_to_block_type(block)
        expected = BlockType.HEADING
        self.assertNotEqual(node, expected)

    def test_quote(self):
        block = """> this is a quote
> so is this"""
        node = block_to_block_type(block)
        expected = BlockType.QUOTE
        self.assertEqual(node, expected)

    def test_unordered_list(self):
        block = """* here is something in list form
- so is this"""
        node = block_to_block_type(block)
        expected = BlockType.UNORDERED_LIST
        self.assertEqual(node, expected)

    def test_ordered_list(self):
        block = """1. here is the first bit
2. here is the second
3. and a third for good measure"""
        node = block_to_block_type(block)
        expected = BlockType.ORDERED_LIST
        self.assertEqual(node, expected)

    def test_code_block(self):
        block = """```
        looks at all this code
        ```"""
        node = block_to_block_type(block)
        expected = BlockType.CODE
        self.assertEqual(node, expected)