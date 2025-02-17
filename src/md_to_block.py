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