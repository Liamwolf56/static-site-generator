from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        remaining = text
        for alt, src in images:
            before, remaining = remaining.split(f"![{alt}]({src})", 1)
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, src))
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes

