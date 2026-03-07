import os
import re

directory = r'c:\Users\Comp\silverbowl'
files = []
for root, _, filenames in os.walk(directory):
    for f in filenames:
        if f.endswith('.html'):
            files.append(os.path.join(root, f))

count = 0
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine relative path prefix for /blog
    if 'blog' in filepath:
        prefix = 'index.html'
        home_prefix = '../index.html'
    else:
        prefix = 'blog/index.html'
        home_prefix = 'index.html'

    new_nav = f'''<ul class="nav-menu" id="nav-menu">
                <li><a href="{home_prefix}">Home</a></li>
                <li><a href="{prefix}?cat=football">Football</a></li>
                <li><a href="{prefix}?cat=youtube">YouTube</a></li>
                <li><a href="{prefix}?cat=crypto">Crypto</a></li>
                <li><a href="{prefix}?cat=forex">Forex & Stocks</a></li>
                <li><a href="{prefix}?cat=makemoney">Make Money</a></li>
                <li><a href="{prefix}?cat=tools">Tools</a></li>
            </ul>'''

    # Replace the existing nav-menu
    new_content = re.sub(r'<ul class="nav-menu" id="nav-menu">.*?</ul>', new_nav, content, flags=re.DOTALL)
    if new_content != content:
        count += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f'Updated nav menu in {count} files out of {len(files)}.')
