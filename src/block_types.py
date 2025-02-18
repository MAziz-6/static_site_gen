import re



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