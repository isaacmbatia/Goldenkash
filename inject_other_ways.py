import os
import re
import json
import random

# Load categories to get all available files
with open(r'c:\Users\Comp\silverbowl\category_map.json', 'r') as f:
    categories = json.load(f)

# Build a mapping of file -> category and file -> title
file_to_title = {}
all_files = []

blog_dir = r'c:\Users\Comp\silverbowl\blog'
for cat, files in categories.items():
    for filename in files:
        all_files.append(filename)
        # Extract title
        filepath = os.path.join(blog_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                title_match = re.search(r'<h1>(.*?)</h1>', content)
                if title_match:
                    short_title = title_match.group(1).split(':')[0] # Get main part of title
                    file_to_title[filename] = short_title
                else:
                    file_to_title[filename] = filename.replace('.html', '').replace('-', ' ').title()

# Now, update each file's content area
count = 0
for filename in all_files:
    filepath = os.path.join(blog_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Other Ways to Make Money" in content:
        continue # Skip if already injected
        
    # Get 3 random files to link to (excluding this one)
    related_files = [f for f in all_files if f != filename]
    picks = random.sample(related_files, 3)
    
    links_html = '\n                <h2>Other Ways to Make Money</h2>\n                <ul>\n'
    for pick in picks:
        title = file_to_title[pick]
        links_html += f'                    <li><strong><a href="{pick}">{title}</a></strong></li>\n'
    links_html += '                </ul>\n'
                    
    # Inject right before <div class="share-bar">
    pattern = r'(<div class="share-bar">)'
    
    new_content = re.sub(pattern, links_html + r'\1', content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Injected 'Other Ways' text into {count} articles.")
