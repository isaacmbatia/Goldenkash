import os
import re

# Fix all remaining files that still use cat=youtube or show "YouTube" as a nav label

search_dirs = [
    'c:/Users/Comp/silverbowl',
    'c:/Users/Comp/silverbowl/_includes',
]

for d in search_dirs:
    for fname in os.listdir(d):
        if not fname.endswith('.html'):
            continue
        path = os.path.join(d, fname)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        updated = content

        # Replace nav link + label  (root pages have blog/ prefix, blog pages don't)
        updated = re.sub(
            r'((?:blog/)?index\.html\?cat=)youtube(">)YouTube(</a>)',
            r'\1socials\2Socials Blogs\3',
            updated
        )
        # catch any leftover bare cat=youtube
        updated = updated.replace('cat=youtube', 'cat=socials')

        # Fix breadcrumb span
        updated = updated.replace('<span>YouTube</span>', '<span>Socials Blogs</span>')

        # Fix tag span
        updated = updated.replace('<span class="tag">YouTube</span>', '<span class="tag">Socials Blogs</span>')

        if updated != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Fixed: {path}")

print("Done.")
