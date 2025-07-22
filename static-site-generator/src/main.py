# src/main.py
import sys
from generate_pages_recursive import generate_pages_recursive
from copy_static import copy_static_contents

def main():
    # Base path defaults to "/"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        if not basepath.endswith("/"):
            basepath += "/"

    content_dir = "content/"
    template_path = "template.html"
    output_dir = "docs/"

    print(f"Using basepath: {basepath}")

    generate_pages_recursive(content_dir, template_path, output_dir, basepath)
    copy_static_contents("static", output_dir)

if __name__ == "__main__":
    main()

