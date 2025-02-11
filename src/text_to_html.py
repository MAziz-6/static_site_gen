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
        case TextType.CODE:
            LeafNode(tag="code",value=text_node.value)
        case TextType.LINK:
            LeafNode(tag="a",value=text_node.value, props=text_node.props)
        case TextType.IMAGES:
            LeafNode(tag="img",value=None, )