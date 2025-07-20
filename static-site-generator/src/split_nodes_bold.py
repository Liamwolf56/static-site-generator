from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

def split_nodes_bold(old_nodes):
    return split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

