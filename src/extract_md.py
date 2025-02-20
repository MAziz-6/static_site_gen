import re

def extract_markdown_images(text):
    if text == None:
        raise ValueError("Text cannot be None")
    return list(re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
    
def extract_markdown_links(text):
    if text == None:
        raise ValueError("Text cannot be None")
    return list(re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text))

def extract_title(text):
    titles = []
    for line in text.splitlines():
        h1 = re.match(r"^# (?!#)(.*)$", line)
        if h1:
            title = h1.group(1).strip()
            titles.append(title)
    if len(titles) == 0: 
        raise Exception("No h1 Header found")
    return titles[0]
