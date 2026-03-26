import os

def remove_recommended_tools():
    blog_dir = r"c:\Users\Comp\silverbowl\blog"
    # The section starts with <!-- Recommended Tools Section --> and ends with </section>
    # However, replacing the exact block is safer.
    
    tools_section_pattern = """
    <!-- Recommended Tools Section -->
    <section class="recommended-tools" style="margin-top: 4rem; padding: 3rem; background: #f8f9fc; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;">
            <div style="font-size: 3.5rem;">🛠️</div>
            <div style="flex: 1; min-width: 250px;">
                <h3 style="margin: 0 0 0.5rem 0; color: #1e293b; font-size: 1.5rem;">Level Up Your Earnings with the Right Tools</h3>
                <p style="margin: 0 0 1.5rem 0; color: #475569; font-size: 1rem; line-height: 1.6;">We've vetted the 50 most powerful tools for making money online in 2026. See the full list and our "Pro Tips" for each.</p>
                <a href="top-50-tools.html" style="background: #6366f1; color: white; padding: 0.8rem 1.8rem; border-radius: 8px; text-decoration: none; display: inline-block; font-weight: 700; transition: background 0.3s ease;">View the 50 Best Tools →</a>
            </div>
        </div>
    </section>
"""

    files = [f for f in os.listdir(blog_dir) if f.endswith(".html")]
    
    count = 0
    for filename in files:
        filepath = os.path.join(blog_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "<!-- Recommended Tools Section -->" in content:
                # Use a simpler way if the exact string doesn't match perfectly (though it should)
                # Let's try to find the comment and the next </section>
                import re
                new_content = re.sub(r'\s*<!-- Recommended Tools Section -->.*?/section>\s*', '\n    ', content, flags=re.DOTALL)
                
                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print(f"Successfully removed from {count} files.")

if __name__ == "__main__":
    remove_recommended_tools()
