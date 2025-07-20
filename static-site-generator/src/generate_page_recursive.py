import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path="/"):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path) and entry.endswith(".md"):
            # Create corresponding .html filename in dest
            relative_path = os.path.relpath(entry_path, dir_path_content)
            dest_file_path = os.path.join(dest_dir_path, relative_path[:-3] + ".html")

            print(f"Generating page: {entry_path} -> {dest_file_path}")
            generate_page(entry_path, template_path, dest_file_path, base_path)

        elif os.path.isdir(entry_path):
            new_dest_dir = os.path.join(dest_dir_path, entry)
            os.makedirs(new_dest_dir, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, new_dest_dir, base_path)

