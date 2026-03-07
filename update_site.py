import os
import re
import json

base = 'c:/Users/Comp/silverbowl'

# ─────────────────────────────────────────────
# 1. Rename "Socials Blogs" → "Social Media" + "cat=socials" stays the same
#    but update display labels in all HTML files
# ─────────────────────────────────────────────
replacements = [
    ('Socials Blogs</a>', 'Social Media</a>'),
    ('>Socials Blogs<', '>Social Media<'),      # h4, spans, etc.
    ('Socials Blogs</span>', 'Social Media</span>'),
]

dirs = [base, os.path.join(base, 'blog'), os.path.join(base, '_includes')]
changed = 0
for d in dirs:
    if not os.path.isdir(d):
        continue
    for fname in os.listdir(d):
        if not fname.endswith('.html'):
            continue
        path = os.path.join(d, fname)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        updated = content
        for old, new in replacements:
            updated = updated.replace(old, new)
        if updated != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(updated)
            changed += 1

print(f"Renamed labels in {changed} HTML files.")

# ─────────────────────────────────────────────
# 2. Rebuild sitemap.xml with ALL blog articles
# ─────────────────────────────────────────────
DOMAIN = 'https://goldenkash.com'

blog_dir = os.path.join(base, 'blog')
blog_files = sorted(
    f for f in os.listdir(blog_dir)
    if f.endswith('.html') and f != 'index.html'
)

sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                 '  <!-- Main Pages -->']
main_pages = [
    ('', '1.0', 'weekly'),
    ('start-here.html', '0.9', 'monthly'),
    ('blog/index.html', '0.9', 'daily'),
    ('resources.html', '0.8', 'monthly'),
    ('about.html', '0.5', 'yearly'),
    ('contact.html', '0.4', 'yearly'),
]
for path, pri, freq in main_pages:
    url = f'{DOMAIN}/{path}' if path else f'{DOMAIN}/'
    sitemap_lines.append(f'  <url><loc>{url}</loc><changefreq>{freq}</changefreq><priority>{pri}</priority></url>')

sitemap_lines.append('  <!-- Blog Articles -->')
for fname in blog_files:
    url = f'{DOMAIN}/blog/{fname}'
    sitemap_lines.append(f'  <url><loc>{url}</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>')

sitemap_lines.append('</urlset>')

sitemap_path = os.path.join(base, 'sitemap.xml')
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sitemap_lines) + '\n')

print(f"Sitemap updated with {len(blog_files)} blog articles.")
