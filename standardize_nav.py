import os
import re

def update_root_nav(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Standardize header for root files
    header_pattern = r'<header class="site-header" id="site-header">.*?</header>'
    
    new_header = """<header class="site-header" id="site-header">
        <div class="header-inner">
            <a href="index.html" class="site-logo">Golden<span>Kash</span></a>
            <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
            <ul class="nav-menu" id="nav-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="blog/index.html?cat=socials">Social Media</a></li>
                <li><a href="blog/index.html?cat=crypto">Crypto</a></li>
                <li><a href="blog/index.html?cat=forex">Forex & Stocks</a></li>
                <li><a href="blog/index.html?cat=makemoney">Make Money</a></li>
                <li><a href="resources.html">Resources</a></li>
                <li><a href="blog/index.html?cat=techai">Tech &amp; AI</a></li>
            </ul>
        </div>
    </header>"""
    
    content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated root nav in {filepath}")

def update_blog_nav(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    header_pattern = r'<header class="site-header" id="site-header">.*?</header>'
    
    new_header = """<header class="site-header" id="site-header">
        <div class="header-inner">
            <a href="../index.html" class="site-logo">Golden<span>Kash</span></a>
            <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
            <ul class="nav-menu" id="nav-menu">
                <li><a href="../index.html">Home</a></li>
                <li><a href="index.html?cat=socials">Social Media</a></li>
                <li><a href="index.html?cat=crypto">Crypto</a></li>
                <li><a href="index.html?cat=forex">Forex & Stocks</a></li>
                <li><a href="index.html?cat=makemoney">Make Money</a></li>
                <li><a href="../resources.html">Resources</a></li>
                <li><a href="index.html?cat=techai">Tech &amp; AI</a></li>
            </ul>
        </div>
    </header>"""
    
    content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_root_nav(r"c:\Users\Comp\silverbowl\index.html")
    update_root_nav(r"c:\Users\Comp\silverbowl\resource.html")
    update_root_nav(r"c:\Users\Comp\silverbowl\resources.html")
    
    blog_dir = r"c:\Users\Comp\silverbowl\blog"
    count = 0
    for f in os.listdir(blog_dir):
        if f.endswith(".html"):
            update_blog_nav(os.path.join(blog_dir, f))
            count += 1
    print(f"Updated nav in {count} blog files.")
