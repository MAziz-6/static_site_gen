import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def are_all_lines_quotes(lines):
    return all(line.strip().startswith(">") for line in lines)

def are_all_lines_unordered_list(lines):
    return all(line.startswith(("* ", "- ")) for line in lines)

def is_code(block):
    return block.startswith("```") and block.endswith("```")

def is_ordered_list(lines):
    if not lines:  # Handle empty string
        return False

    expected_number = 1
    for line in lines:
        match = re.match(rf"^{expected_number}\. ", line)  
        if not match:
            return False
        expected_number += 1
    return True

def block_to_block_type(block):
    block_type = BlockType.PARAGRAPH
    lines = block.split("\n")
    first_line = lines[0]

    match first_line:
        case line if re.match(r"^#{1,6} ", line) :
            block_type = BlockType.HEADING        
        case _:
            if are_all_lines_quotes(lines):
                block_type = BlockType.QUOTE
            elif are_all_lines_unordered_list(lines):
                block_type = BlockType.UNORDERED_LIST
            elif is_code(block):
                block_type = BlockType.CODE
            elif is_ordered_list(lines):
                block_type = BlockType.ORDERED_LIST
            else:
                block_type = BlockType.PARAGRAPH
    return block_type