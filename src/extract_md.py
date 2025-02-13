import re

def extract_markdown_images(text):
    if text == None:
        raise ValueError("Text cannot be None")
    return list(re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
    
def extract_markdown_links(text):
    if text == None:
        raise ValueError("Text cannot be None")
    return list(re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text))