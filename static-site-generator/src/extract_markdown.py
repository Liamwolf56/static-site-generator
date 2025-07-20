import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.strip().startswith("# "):
            return line.strip().lstrip("#").strip()
    raise Exception("No H1 header found.")

