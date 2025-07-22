import os
from generate_page import generate_page

def generate_pages_recursive(content_dir, template_path, dest_dir, basepath="/"):
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                relative_path = os.path.relpath(from_path, content_dir)
                dest_path = os.path.join(dest_dir, relative_path).replace(".md", ".html")

                print(f"Generating page: {from_path} -> {dest_path}")
                generate_page(from_path, template_path, dest_path, basepath)

