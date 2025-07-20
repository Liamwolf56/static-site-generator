import sys
from generate_pages_recursive import generate_pages_recursive
from copy_static import copy_static

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <content_dir> <template_path> <output_dir>")
        sys.exit(1)

    content_dir = sys.argv[1]
    template_path = sys.argv[2]
    output_dir = sys.argv[3]

    # Generate all pages recursively
    generate_pages_recursive(content_dir, template_path, output_dir)

    # Copy static files (like images, css) from static/ folder to output_dir/static/
    copy_static("static", output_dir)

if __name__ == "__main__":
    main()

