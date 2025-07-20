from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        remaining = text
        for text_val, url in links:
            before, remaining = remaining.split(f"[{text_val}]({url})", 1)
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(text_val, TextType.LINK, url))
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

