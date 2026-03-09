import os
import glob
base_dir = r"c:\Users\Comp\silverbowl"

filepath = os.path.join(base_dir, "blog", "ai-side-hustles-2026.html")
print("testing file:", filepath)
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
print("has link rel icon:", '<link rel="icon"' in content)
print("has </head>:", '</head>' in content)
