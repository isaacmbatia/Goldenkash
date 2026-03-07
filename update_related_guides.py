import json
import os
import re
import random

with open(r'c:\Users\Comp\silverbowl\category_map.json', 'r') as f:
    categories = json.load(f)

# Build a mapping of file -> category and file -> title
file_to_cat = {}
file_to_title = {}

blog_dir = r'c:\Users\Comp\silverbowl\blog'
for cat, files in categories.items():
    for filename in files:
        file_to_cat[filename] = cat
        # Extract title
        filepath = os.path.join(blog_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                title_match = re.search(r'<h1>(.*?)</h1>', content)
                if title_match:
                    short_title = title_match.group(1)[:40] + ('...' if len(title_match.group(1)) > 40 else '')
                    file_to_title[filename] = short_title
                else:
                    file_to_title[filename] = filename.replace('.html', '').replace('-', ' ').title()

# Now, update each file's related guides
count = 0
for filename, cat in file_to_cat.items():
    filepath = os.path.join(blog_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Get 3 random related files from the same category
    related_files = [f for f in categories[cat] if f != filename]
    num_to_pick = min(3, len(related_files))
    if num_to_pick == 0:
        continue # skip if no related files
        
    picks = random.sample(related_files, num_to_pick)
    
    related_html = '<div class="widget-title">Related Guides</div>\n'
    for pick in picks:
        title = file_to_title[pick]
        related_html += f'''                    <a href="{pick}" class="popular-post"><span class="pp-num">→</span>
                        <div><div class="pp-title">{title}</div></div>
                    </a>\n'''
                    
    # Replace the existing sidebar-widget for related guides
    # We find <div class="sidebar-widget"> ... </div> right after <div class="toc"> ... </div>
    # Actually, let's just use regex to replace the content of that specific widget.
    
    pattern = r'<div class="sidebar-widget">\s*<div class="widget-title">Related Guides</div>.*?</div>\s*</aside>'
    replacement = f'<div class="sidebar-widget">\n{related_html}                </div>\n            </aside>'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated related guides in {count} articles.")
