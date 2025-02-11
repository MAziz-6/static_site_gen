from enum import Enum
from htmlnode import *
from textnode import TextType

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            LeafNode(tag=None, value=text_node.value)
        case TextType.BOLD:
            LeafNode(tag="b", value=text_node.value)
        case TextType.ITALIC:
            LeafNode(tag="i",value=text_node.value)
        case TextType.ITALIC:
            LeafNode(tag="i",value=text_node.value)