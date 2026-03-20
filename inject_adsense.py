import os
import glob

# AdSense Publisher ID
PUB_ID = "pub-1294582602291166"
SNIPPET = f'''<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB_ID}" crossorigin="anonymous"></script>
'''

def inject_adsense(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already injected
    if PUB_ID in content and 'adsbygoogle.js' in content:
        print(f"Skipping {file_path} (already present)")
        return False
    
    # Insert before </head>
    if '</head>' in content:
        new_content = content.replace('</head>', f'{SNIPPET}</head>')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected AdSense into {file_path}")
        return True
    else:
        print(f"Skipping {file_path} (no </head> found)")
        return False

def main():
    # Find all HTML files
    html_files = glob.glob('*.html') + glob.glob('blog/*.html')
    
    count = 0
    for file_path in html_files:
        if inject_adsense(file_path):
            count += 1
    
    print(f"Successfully injected AdSense into {count} files.")

if __name__ == "__main__":
    main()
