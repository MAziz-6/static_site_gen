import re
from md_to_block import markdown_to_blocks
from block_types import block_to_block_type, BlockType
from htmlnode import ParentNode, HTMLNode, LeafNode
from to_textnode import text_to_textnodes
from text_to_html import text_node_to_html_node

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
        elif type == BlockType.QUOTE:
            node = quote_to_html(block)
            children.append(node)
        else:
            node = paragraph_to_html(block)
            children.append(node)
    final_node = ParentNode(tag="div", children=children)
    return final_node


def heading_to_html(block):
    match = re.match(r"^(#{1,6})\s", block)
    header_counter = len(match.group(1))
    heading_text = block[match.end():].strip()  # Slice after the matched part
    node = LeafNode(tag="h"+ str(header_counter), value=heading_text)
    return node

def paragraph_to_html(block):
    sanitized_text = block.strip()
    text_nodes = text_to_textnodes(sanitized_text)  
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return ParentNode(tag="p", children=children)


def code_to_html(block):
    code_text = re.sub(r"^```|```$", "", block).strip()
    node = LeafNode(tag="code", value=code_text)
    return node

def quote_to_html(block):
    quote_text = re.sub(r"^>\s*", "", block).strip()  # Removes leading `>` followed by spaces
    node = LeafNode(tag="blockquote", value=quote_text)
    return node

def unordered_list_to_html(block):
    children = []
    for item in block.splitlines(): 
        match = re.match(r"^[*-]\s*", item)
        if match:
            cleaned_item = item[match.end():].strip()  # Slice after the match
        else:
            cleaned_item = item.strip()

        # Convert the list item text to text nodes
        text_nodes = text_to_textnodes(cleaned_item)
        item_children = []
        for text_node in text_nodes:
            html_node = text_node_to_html_node(text_node)
            item_children.append(html_node)

        node = ParentNode(tag="li", children=item_children)
        children.append(node)
    ul_node = ParentNode(tag="ul", children=children)
    return ul_node

def ordered_list_to_html(block):
    children = []
    for item in block.splitlines(): 
        match = re.match(r"^\d+\.\s", item)
        if match:
            cleaned_item = item[match.end():].strip() 
        else:
            cleaned_item = item.strip() 
        
        # Convert the list item text to text nodes
        text_nodes = text_to_textnodes(cleaned_item)
        item_children = []
        for text_node in text_nodes:
            html_node = text_node_to_html_node(text_node)
            item_children.append(html_node)

        node = ParentNode(tag="li", children=item_children)
        children.append(node)
    ol_node = ParentNode(tag="ol", children=children)
    return ol_node