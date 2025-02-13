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