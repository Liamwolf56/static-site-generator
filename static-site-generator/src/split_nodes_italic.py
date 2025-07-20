from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

def split_nodes_italic(old_nodes):
    # Split italic nodes using both '*' and '_'
    nodes = split_nodes_delimiter(old_nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    return nodes

