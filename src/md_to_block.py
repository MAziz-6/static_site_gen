import re

def markdown_to_blocks(markdown):
    """
    1) split the lines based on blank lines --can be multiple, not just line breaks
    2) strip any whitespace
    3) remove any empty blocks
    """
    new_blocks = []
    # Split lines based on blank line(s) -- regex time
    blocks = re.split(r"\n\s*\n", markdown)

    for block in blocks:
        if not block.strip():
            continue
        # split into lines
        lines = block.split("\n")
        # strip each line
        cleaned_lines = [line.strip() for line in lines]
        # join back
        cleaned_block = "\n".join(cleaned_lines)
        # add to list
        new_blocks.append(cleaned_block)
    return new_blocks