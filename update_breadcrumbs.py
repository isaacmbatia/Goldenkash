import json
import os
import re

with open(r'c:\Users\Comp\silverbowl\category_map.json', 'r') as f:
    categories = json.load(f)

file_to_cat = {}
blog_dir = r'c:\Users\Comp\silverbowl\blog'
cat_titles = {
    'football': 'Football',
    'youtube': 'YouTube',
    'crypto': 'Crypto',
    'forex': 'Forex & Stocks',
    'makemoney': 'Make Money',
    'tools': 'Tools'
}

for cat, files in categories.items():
    for filename in files:
        file_to_cat[filename] = cat_titles[cat]

count = 0
for filename, cat_title in file_to_cat.items():
    filepath = os.path.join(blog_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for breadcrumb
    # <nav class="breadcrumb"><a href="../index.html">Home</a> <span>›</span> <a href="index.html">Blog</a>
    #            <span>›</span> <span>Side Hustles</span></nav>
    pattern = r'(<nav class="breadcrumb">.*?<span>›</span>\s*<span>)(.*?)(</span>\s*</nav>)'
    
    def replacer(match):
        return match.group(1) + cat_title + match.group(3)
        
    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated breadcrumbs in {count} articles.")
