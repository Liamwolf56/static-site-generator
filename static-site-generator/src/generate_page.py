import os
from extract_markdown import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown content
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    # Read the HTML template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Convert markdown to an HTMLNode tree and then to HTML string
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    # Extract title from markdown
    title = extract_title(markdown)

    # Insert title and HTML content into template placeholders
    output = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    # Fix absolute links for base path (useful for GitHub Pages)
    output = output.replace('href="/', f'href="{base_path}')
    output = output.replace('src="/', f'src="{base_path}')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the generated HTML page
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

