import os
import glob

base_dir = r"c:\Users\Comp\silverbowl"

def inject_favicon(filepath, is_blog):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<link rel="icon"' in content:
        # Check if we should fix absolute path to relative if it was wrongly injected earlier (not likely but good to be careful)
        return

    favicon_link = '../img/favicon.png' if is_blog else 'img/favicon.png'
    tag = f'    <link rel="icon" type="image/png" href="{favicon_link}" />\n'

    if '</head>' in content:
        content = content.replace('</head>', tag + '</head>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected in {os.path.basename(filepath)}")
    else:
        print(f"Warning: no </head> found in {os.path.basename(filepath)}")

count = 0
for root_file in glob.glob(os.path.join(base_dir, "*.html")):
    inject_favicon(root_file, False)
    count += 1

blog_count = 0
for blog_file in glob.glob(os.path.join(base_dir, "blog", "*.html")):
    inject_favicon(blog_file, True)
    blog_count += 1

print(f"Processed {count} root files and {blog_count} blog files.")
