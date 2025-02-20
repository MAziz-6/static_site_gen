import os
from md_to_html import markdown_to_html_node
from extract_md import extract_title



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # read contents of the markdown file and template
    with open(from_path, 'r') as file:
        md = file.read()
    with open(template_path, 'r') as file:
        template = file.read()

    # create an html string of the mkdown file
    node = markdown_to_html_node(md)
    content = node.to_html()
    
    # extract the title for the page
    title = extract_title(md)

    # replace the title and content in the template
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    # make sure the directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # write the final_html to the destination
    with open(dest_path, 'w') as file:
        file.write(final_html)


# def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
#     for item in os.listdir(dir_path_content):
#         content_path = os.path.join(dir_path_content, item)
#         dest_path = os.path.join(dest_dir_path, item)
#         if os.path.isdir(content_path):
#             if not os.path.exists(dest_path):
#                 os.makedirs(dest_path)
#             generate_pages_recursive(content_path, template_path, dest_path)
        
#         if content_path.endswith(".md") or content_path.endswith(".markdown"):
#             name, ext = os.path.splitext(item)
#             new_name = name + ".html"
#             new_path = os.path.join(dest_dir_path, new_name)
#             generate_page(content_path, template_path, new_path)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Processing directory: {dir_path_content}")
    for item in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        print(f"Looking at: {content_path}")
        
        if os.path.isdir(content_path):
            print(f"Found directory: {content_path}")
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            generate_pages_recursive(content_path, template_path, dest_path)
        
        if content_path.endswith(".md") or content_path.endswith(".markdown"):
            print(f"Processing markdown file: {content_path}")
            name, ext = os.path.splitext(item)
            new_name = name + ".html"
            new_path = os.path.join(dest_dir_path, new_name)
            generate_page(content_path, template_path, new_path)