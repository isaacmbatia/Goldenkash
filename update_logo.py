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

    # Case-insensitive replacement of GOLDEN<span>KASH.com</span> to Golden<span>Kash</span>
    new_content = re.sub(r'GOLDEN<span>KASH\.com</span>', r'Golden<span>Kash</span>', content, flags=re.IGNORECASE)
    
    # Also fix plain text mentions of the site name in meta tags, paragraphs, footer etc.
    # Exclude URLs like https://goldenkash.com
    # We will just replace GOLDENKASH.com and goldenkash.com where it is not part of a URL
    # A simple approach for this site size:
    new_content = re.sub(r'(?<!https://)GOLDENKASH\.com', 'GoldenKash', new_content)
    new_content = re.sub(r'(?<!https://)goldenkash\.com', 'GoldenKash', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated logo in {count} files.")
