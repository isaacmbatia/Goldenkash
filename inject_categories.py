import json
import re

with open(r'c:\Users\Comp\silverbowl\category_map.json', 'r') as f:
    categories = json.load(f)

# reverse map
file_to_cat = {}
for cat, files in categories.items():
    for file in files:
        file_to_cat[file] = cat

filepath = r'c:\Users\Comp\silverbowl\blog\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# find all post cards
# pattern: <a href="filename.html" class="card post-card">
pattern = r'<a href="([^"]+)" class="card post-card">'

def replacer(match):
    filename = match.group(1)
    cat = file_to_cat.get(filename, 'makemoney') # default
    return f'<a href="{filename}" class="card post-card" data-category="{cat}">'

new_content = re.sub(pattern, replacer, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated post cards with data-category attributes.")
