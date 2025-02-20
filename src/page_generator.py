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