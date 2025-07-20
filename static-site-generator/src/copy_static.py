import os
import shutil

def copy_static(src_dir: str, dest_dir: str) -> None:
    if os.path.exists(dest_dir):
        print(f"Removing existing directory: {dest_dir}")
        shutil.rmtree(dest_dir)

    print(f"Creating destination directory: {dest_dir}")
    os.makedirs(dest_dir)

    def recursive_copy(src, dest):
        for entry in os.listdir(src):
            src_path = os.path.join(src, entry)
            dest_path = os.path.join(dest, entry)
            if os.path.isdir(src_path):
                print(f"Creating directory: {dest_path}")
                os.makedirs(dest_path)
                recursive_copy(src_path, dest_path)
            elif os.path.isfile(src_path):
                print(f"Copying file: {src_path} to {dest_path}")
                shutil.copy(src_path, dest_path)

    recursive_copy(src_dir, dest_dir)

