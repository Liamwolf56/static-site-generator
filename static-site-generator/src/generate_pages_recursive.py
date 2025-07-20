import os
from generate_page import generate_page

def generate_pages_recursive(content_dir: str, template_path: str, output_dir: str) -> None:
    """
    Recursively generate HTML pages for all markdown files under content_dir,
    using the template_path, and outputting to output_dir preserving structure.
    """
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)

                # Calculate relative path from content_dir for output
                rel_path = os.path.relpath(md_path, content_dir)
                # Change .md to .html
                rel_path_html = rel_path[:-3] + ".html"

                # Output path in output_dir
                output_path = os.path.join(output_dir, rel_path_html)

                # Ensure output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                print(f"Generating page: {md_path} -> {output_path}")
                generate_page(md_path, template_path, output_path)

