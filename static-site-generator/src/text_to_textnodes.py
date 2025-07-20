from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from split_nodes_code import split_nodes_code
from split_nodes_bold import split_nodes_bold
from split_nodes_italic import split_nodes_italic

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_code(nodes)
    nodes = split_nodes_bold(nodes)
    nodes = split_nodes_italic(nodes)
    return nodes

