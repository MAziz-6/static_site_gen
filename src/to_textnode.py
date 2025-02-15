from splitnodes import *
from textnode import *

def text_to_textnodes(text): 
    node = TextNode(text, TextType.TEXT)

    # Process images and links first
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)

    # Process Remaining Text Types:
    # Bold
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    # Italic
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    # Code
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)

    return new_nodes


text = "This is **bold *italic* bold**"
nodes = text_to_textnodes(text)
for node in nodes:
    print(f"Text: '{node.text}', Type: {node.text_type}")

    