import os
import re

def migrate_tools_page():
    blog_file = r"c:\Users\Comp\silverbowl\blog\top-50-tools.html"
    root_file = r"c:\Users\Comp\silverbowl\resource.html"
    
    with open(blog_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update paths
    # CSS and Images
    content = content.replace("../css/", "css/")
    content = content.replace("../img/", "img/")
    
    # Header links
    content = content.replace('href="../index.html"', 'href="index.html"')
    # Category links in header (now need blog/ prefix)
    content = content.replace('href="index.html?cat=', 'href="blog/index.html?cat=')
    
    # Canonical link
    content = content.replace('https://goldenkash.com/blog/top-50-tools.html', 'https://goldenkash.com/resource.html')
    
    # Footer links (if they were relative)
    content = content.replace('href="../privacy-policy.html"', 'href="privacy-policy.html"')
    content = content.replace('href="../disclaimer.html"', 'href="disclaimer.html"')
    content = content.replace('href="../terms.html"', 'href="terms.html"')
    content = content.replace('href="../about.html"', 'href="about.html"')
    content = content.replace('href="../start-here.html"', 'href="start-here.html"')
    
    # Related guide links in tool cards (they are inside the same folder currently, now need blog/)
    # Example: <a href="how-to-use-chatgpt-for-side-hustles.html" class="related-guide">
    # We should only target links that don't have http or / or ../
    def link_replacer(match):
        link = match.group(1)
        if not (link.startswith("http") or link.startswith("/") or link.startswith("#") or link.startswith("..")):
            return f'href="blog/{link}"'
        return match.group(0)

    content = re.sub(r'href="([^"]+\.html)"', link_replacer, content)
    
    # Specific fix for blog/index.html in the tools nav if it was there (it uses anchor links currently)
    # But let's check the header in resource.html again.
    
    with open(root_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Migrated to {root_file}")

def update_other_links():
    index_file = r"c:\Users\Comp\silverbowl\index.html"
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace('blog/top-50-tools.html', 'resource.html')
    
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated index.html links")

if __name__ == "__main__":
    migrate_tools_page()
    update_other_links()
