import re
import os

filepath = r'c:\Users\Comp\silverbowl\blog\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_links = [
    'start-microgreens-business.html',
    'van-life-budget-guide-2026.html',
    'house-hacking-guide-2026.html',
    'core-and-satellite-portfolio.html',
    'mega-backdoor-roth-ira-2026.html',
    'cybersecurity-small-business-audits.html',
    'fractional-coo-startups.html',
    'ugc-creator-guide.html'
]

count = 0
for link in old_links:
    pattern = r'<a href="' + link + r'".*?</a>'
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    if new_content != content:
        count += 1
    content = new_content

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

deleted_files = 0
for link in old_links:
    path = os.path.join(r'c:\Users\Comp\silverbowl\blog', link)
    if os.path.exists(path):
        os.remove(path)
        deleted_files += 1

print(f'Old links excised: {count}')
print(f'Old files deleted: {deleted_files}')
