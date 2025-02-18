import re

def markdown_to_blocks(markdown):
    new_blocks = []
    # Split lines based on blank line(s)
    blocks = re.split(r"\n\s*\n", markdown)

    for block in blocks:
        # Skip empty blocks
        if not block.strip():
            continue
        # Split into lines and clean each line
        lines = block.split("\n")
        # Strip each line and remove any empty lines
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        # Join back together
        cleaned_block = "\n".join(cleaned_lines)
        # Only append if we have content
        if cleaned_block:
            new_blocks.append(cleaned_block)
    return new_blocks

def are_all_lines_quotes(lines):
    return all(line.startswith(">") for line in lines)

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
    block_type = None
    lines = block.split("\n")
    first_line = lines[0]

    match first_line:
        case line if re.match(r"^#{1,6} ", line) :
            block_type = "heading"        
        case _:
            if are_all_lines_quotes(lines):
                block_type = "quote"
            elif are_all_lines_unordered_list(lines):
                block_type = "unordered_list"
            elif is_code(block):
                block_type = "code"
            elif is_ordered_list(lines):
                block_type = "ordered_list"
            else:
                block_type = "paragraph"
    return block_type