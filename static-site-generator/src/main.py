import sys
import os
from generate_pages_recursive import generate_pages_recursive
from copy_static import copy_static

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    content_dir = "./content"
    template_path = "./template.html"
    output_dir = "./docs"  # <-- change from /public to /docs

    if os.path.exists(output_dir):
        print(f"Removing existing directory: {os.path.abspath(output_dir)}")
        os.system(f"rm -rf {output_dir}")
    print(f"Creating destination directory: {os.path.abspath(output_dir)}")
    os.makedirs(output_dir, exist_ok=True)

    copy_static("./static", output_dir)
    generate_pages_recursive(content_dir, template_path, output_dir, base_path)

if __name__ == "__main__":
    main()

