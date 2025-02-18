import re
from md_to_block import markdown_to_blocks
from block_types import block_to_block_type, BlockType
from htmlnode import ParentNode, HTMLNode

def markdown_to_html_node(markdown):
    """
    Converts an entire Markdown document into a single
    HTML node.
    """
    # Start by breaking down the document into blocks
    blocks = markdown_to_blocks(markdown)
    children = []
    # Loop over each block
    for block in blocks:
        # First determine the block type
        type = block_to_block_type(block)
        # Based on the block type found, create a new HTMLNode 
        if type == BlockType.HEADING:
            node = heading_to_html(block)
            children.append(node)
        elif type == BlockType.UNORDERED_LIST:
            node = unordered_list_to_html(block)
            children.append(node)
        elif type == BlockType.ORDERED_LIST:
            node = ordered_list_to_html(block)
            children.append(node)
        elif type == BlockType.CODE:
            node = code_to_html(block)
            children.append(node)
        else:
            node = paragraph_to_html(block)
            children.append(node)
        final_node = ParentNode(tag="div", children=children)
    return final_node


def heading_to_html(block):
    match = re.match(r"^(#{1,6})\s", block)
    header_counter = len(match.group(1))
    node = HTMLNode(tag="h"+ str(header_counter), value=block)
    return node

def paragraph_to_html(block):
    return HTMLNode(tag="p", value=block)

def code_to_html(block):
    return HTMLNode(tag="code", value=block)

def quote_to_html(block):
    return HTMLNode(tag="blockquote", value=block)

def unordered_list_to_html(block):
    children = []
    for item in block:
        cleaned_item = item.lstrip("*-").strip()
        node = HTMLNode(tag="li", value=cleaned_item)
        children.append(node)
    ul_node = ParentNode(tag="ul",children=children)
    return ul_node

def ordered_list_to_html(block):
    children = []
    for item in block:
        cleaned_item = item.lstrip(re.match(r"^\d+\.\s", item).group(0)).strip()
        node = HTMLNode(tag="li", value=cleaned_item)
        children.append(node)
    ol_node = ParentNode(tag="ol",children=children)
    return ol_node