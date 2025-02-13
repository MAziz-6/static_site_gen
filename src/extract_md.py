import re

def extract_markdown_images(text):
    return list(re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
    
def extract_markdown_links(text):
    return list(re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text))