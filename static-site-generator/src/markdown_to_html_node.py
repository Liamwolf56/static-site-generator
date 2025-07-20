from htmlnode import HTMLNode, LeafNode, ParentNode
from block_type import BlockType, block_to_block_type
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def text_to_children(text):
    """
    Converts inline markdown text into a list of HTMLNodes.
    """
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in text_nodes]


def heading_to_html_node(block):
    # Count number of leading '#' characters
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    # Extract heading text after '# ' characters
    content = block[level + 1 :].strip()
    children = text_to_children(content)
    return ParentNode(f"h{level}", children)


def code_block_to_html_node(block):
    # Remove starting and ending triple backticks
    lines = block.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    code_text = "\n".join(lines)
    # No inline markdown parsing for code block content
    code_node = text_node_to_html_node(TextNode(code_text, TextType.TEXT))
    code_tag = ParentNode("code", [code_node])
    pre_tag = ParentNode("pre", [code_tag])
    return pre_tag


def quote_block_to_html_node(block):
    # Remove leading '>' and optional space from each line
    lines = block.splitlines()
    stripped_lines = [line[1:].lstrip() if line.startswith(">") else line for line in lines]
    content = "\n".join(stripped_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block):
    lines = block.splitlines()
    items = []
    for line in lines:
        content = line[2:].strip()  # Remove '- ' prefix
        children = text_to_children(content)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)


def ordered_list_to_html_node(block):
    lines = block.splitlines()
    items = []
    for line in lines:
        dot_index = line.find(". ")
        if dot_index == -1:
            raise ValueError(f"Invalid ordered list item: {line}")
        content = line[dot_index + 2 :].strip()
        children = text_to_children(content)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)


def paragraph_to_html_node(block):
    children = text_to_children(block)
    return ParentNode("p", children)


def markdown_to_html_node(markdown):
    """
    Converts full markdown text into a parent HTMLNode with nested children.
    """
    # Split markdown into blocks by two newlines, stripping whitespace and ignoring empty blocks
    blocks = [b.strip() for b in markdown.strip().split("\n\n") if b.strip()]
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            node = heading_to_html_node(block)
        elif block_type == BlockType.CODE:
            node = code_block_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            node = quote_block_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = unordered_list_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            node = ordered_list_to_html_node(block)
        elif block_type == BlockType.PARAGRAPH:
            node = paragraph_to_html_node(block)
        else:
            raise ValueError(f"Unknown block type: {block_type}")

        children.append(node)

    # Wrap all block nodes in a single <div>
    return ParentNode("div", children)

