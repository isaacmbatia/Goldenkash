import os

def update_navigation():
    # Update root files
    root_files = [r"c:\Users\Comp\silverbowl\index.html", r"c:\Users\Comp\silverbowl\resource.html", r"c:\Users\Comp\silverbowl\resources.html"]
    
    for filepath in root_files:
        if not os.path.exists(filepath): continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace Tools with Resources in Nav
        # index.html active/inactive links
        content = content.replace('<li><a href="resource.html">Tools</a></li>', '<li><a href="resources.html">Resources</a></li>')
        content = content.replace('<li><a href="resources.html">Tools</a></li>', '<li><a href="resources.html">Resources</a></li>')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated nav in {filepath}")

    # Update blog files
    blog_dir = r"c:\Users\Comp\silverbowl\blog"
    blog_files = [f for f in os.listdir(blog_dir) if f.endswith(".html")]
    
    count = 0
    for filename in blog_files:
        filepath = os.path.join(blog_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace Tools with Resources in Nav (blog files use ../)
        new_content = content.replace('<li><a href="../resource.html">Tools</a></li>', '<li><a href="../resources.html">Resources</a></li>')
        new_content = new_content.replace('<li><a href="../resources.html">Tools</a></li>', '<li><a href="../resources.html">Resources</a></li>')
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            
    print(f"Updated nav in {count} blog files.")

if __name__ == "__main__":
    update_navigation()
