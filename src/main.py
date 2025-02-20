from textnode import *
import os
import shutil
from page_generator import generate_page

this_dir = os.path.dirname(__file__)
destination = os.path.normpath(os.path.join(this_dir,"..","public"))
source_location = os.path.normpath(os.path.join(this_dir, "..", "static"))
template_path = os.path.normpath(os.path.join(this_dir, "..", "template.html"))
md_path = os.path.normpath(os.path.join(this_dir, "..", "content", "index.md"))
html_dest = os.path.normpath(os.path.join(destination, "index.html"))

def delete_directory(deletion_location):
    try:
        if os.path.exists(deletion_location):
            shutil.rmtree(deletion_location)
            print(f"Deleted directory: {deletion_location}")
        else:
            print(f"Directory {deletion_location} does not exist")
    except Exception as e:
        print(f"Dir Deletion failed: {e}")
        pass

def copy_contents(src, dest):
    os.makedirs(dest)
    for item in os.listdir(src):
        source_path = os.path.join(src, item)
        destination_path = os.path.join(dest, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied file: {source_path} and moved to {destination_path}")
        elif os.path.isdir(source_path):
            shutil.copytree(source_path, destination_path)
            print(f"Copied dir: {source_path} and moved to {destination_path}")
    print(f"Everything from {source_path} has been copied to {destination_path}")
    return

def test_setup(from_here, deletion_location, to_here):
    try:
        if not os.path.exists(from_here):
            os.makedirs(from_here)
        
        if not os.path.exists(deletion_location):
            os.makedirs(deletion_location)

        if not os.path.exists(to_here):
            os.makedirs(to_here)
        
        with open(os.path.join(from_here, "t1.py"),"w") as f:
            pass
        with open(os.path.join(from_here, "t2.py"),"w") as f:
            pass
    except Exception as e:
        print(e)
        exit()


def main():
    # First, delete the destination directory
    delete_directory(destination)
    # Next, create/copy everything from soure to new destination dir
    copy_contents(source_location, destination)
    # Generate the page from content/index.md using template.html and write to public
    generate_page(md_path, template_path, html_dest)

if __name__ == "__main__":
    main()