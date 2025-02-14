import re
from textnode import TextNode, TextType
from htmlnode import HTMLNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    childlist = []
    for node in old_nodes:
        # Handles non text types to start
        if node.text_type != TextType.TEXT:
            childlist.append(node)
            continue
        
        # split based on delim
        nl = node.text.split(delimiter)

        # Check for unmatched delims
        if len(nl) % 2 == 0: 
            raise ValueError(f"Unmatched delimiter in text: {node.text}")
        
        # Alternating text_type for list
        toggle_type = TextType.TEXT     # Start with text type
        for segment in nl:
            childlist.append(TextNode(segment, toggle_type))
            toggle_type = text_type if toggle_type == TextType.TEXT else TextType.TEXT
    return childlist


def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    new_nodes = []
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for node in old_nodes:
        last_end = 0    # Tracks position of processed text
        text = node.text
        
        # Handle no matches (user error)
        if not re.search(pattern, text):    # If nothing matches
            new_nodes.append(node)          # add this node as is
            continue                        # skip the rest

        for match in re.finditer(pattern, text):
            # This first section is for the text portion (not matched to regex)
            if last_end < match.start():
                text_bit = text[last_end:match.start()]     # Extract the text before the match to regex
                if text_bit:
                    new_nodes.append(TextNode(text_bit, TextType.TEXT))

            # Next we will deal with matched bits
            link_text = match.group(1)  # The text inside the brackets []
            link_href = match.group(2)  # The URL inside the parentheses ()
            new_nodes.append(TextNode(link_text, TextType.LINK, link_href))

            # update the last_end position
            last_end = match.end()

        # Update any text after the last link
        if last_end < len(text):
            remaining_text = text[last_end:]    # split from final link onward
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes