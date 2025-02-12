from textnode import TextNode, TextType
from htmlnode import HTMLNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    childlist = []
    for node in old_nodes:
        nl = node.text.split(delimiter)
        toggle_type = TextType.TEXT     # Start with text type
        for segment in nl:
            childlist.append(TextNode(segment, toggle_type))
            toggle_type = text_type if toggle_type == TextType.TEXT else TextType.TEXT
    return childlist