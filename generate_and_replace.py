import os
import re
import json

titles = [
    # High Traffic
    "Top 10 Cryptocurrencies to Watch in 2026",
    "Beginner’s Guide to Crypto Investing: How to Start Safely",
    "Is Bitcoin Still Worth Buying? Expert Insights",
    "Ethereum vs. Solana: Which Blockchain Wins in 2026?",
    "Crypto Trading Strategies That Actually Work",
    "How to Spot the Next Altcoin Boom",
    "The Future of DeFi: Opportunities and Risks",
    "Crypto Scams to Avoid in 2026",
    "NFTs Explained: Are They Still Relevant?",
    "Best Crypto Wallets for Security and Ease of Use",
    # Evergreen
    "How to Make Passive Income with Crypto Staking",
    "Crypto Regulations in Africa: What You Need to Know",
    "5 Ways to Earn Crypto Without Trading",
    "Blockchain Technology Beyond Bitcoin: Real‑World Uses",
    "Crypto Mining in 2026: Still Profitable?"
]

def create_slug(title):
    s = title.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    return s.strip('-') + '.html'

def generate_article_content(title):
    return f"""
                <p>Welcome to our comprehensive guide on <strong>{title}</strong>. As the cryptocurrency landscape continues to evolve rapidly in 2026, staying informed is the key to maximizing your investments and minimizing risks.</p>
                <p>Whether you're looking into Bitcoin, Ethereum, Solana, or exploring decentralized finance (DeFi) and NFTs, the opportunities in the crypto space are massive. However, it requires a strategic approach, a clear understanding of the technology, and robust security practices to succeed.</p>
                
                <h2 id="key-insights">Key Insights and Strategies</h2>
                <p>To truly grasp the potential of this topic, you have to look beyond the hype. Here are some of the fundamental elements that drive success in the current crypto environment:</p>
                <ul>
                    <li><strong>Research and Due Diligence:</strong> Always look into the team, technology, and real-world use case behind any blockchain project before investing your capital.</li>
                    <li><strong>Risk Management:</strong> Never invest money you can't afford to lose. Cryptocurrency markets are highly volatile, and diversifying your portfolio is crucial.</li>
                    <li><strong>Security First:</strong> Utilize hardware wallets for your long-term crypto holdings. Keep your private keys offline and be extremely cautious of phishing links.</li>
                </ul>

                <h2 id="opportunities">Future Opportunities</h2>
                <p>The blockchain ecosystem in 2026 offers more than just speculative trading. We are seeing incredible advancements in decentralized applications, staking yields, and regulatory clarity across the globe, especially in regions rapidly adopting digital assets like Africa and Latin America.</p>
                <p>By understanding the narratives, you position yourself ahead of the curve. Keep an eye on institutional adoption, Layer 2 scaling solutions, and the seamless integration of blockchain technology into traditional finance.</p>
                
                <h2 id="conclusion">Final Thoughts</h2>
                <p>Success in crypto is a marathon, not a sprint. Take your time to build your knowledge base, utilize secure wallets, and approach the market with a calm and analytical mindset. Remember, the most profitable investors are those who manage their emotions and stick to their long-term strategies.</p>

                <h2>Other Ways to Make Money</h2>
                <ul>
                    <li><strong><a href="dropshipping-shopify.html">How to Start Dropshipping with Shopify</a></strong></li>
                    <li><strong><a href="affiliate-marketing-beginners.html">Affiliate Marketing for Beginners — A Step-by-Step Guide</a></strong></li>
                    <li><strong><a href="20-ways-make-100-online.html">20 Legit Ways to Make $100 Online</a></strong></li>
                </ul>
                <div class="share-bar"><span>Share:</span><a class="share-btn share-tw" href="#"
                        target="_blank">Twitter</a><a class="share-btn share-wa" href="#" target="_blank">WhatsApp</a>
                </div>
                <div class="tags-row"><span class="tag">Crypto</span><span class="tag">Investing</span><span
                        class="tag">Finance</span></div>
"""

template_path = 'c:/Users/Comp/silverbowl/blog/watch-videos-earn-money.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Replace socials inside template before generating to save time
template = template.replace('cat=youtube">YouTube</a>', 'cat=socials">Socials Blogs</a>')
template = template.replace('cat=youtube">YouTube', 'cat=socials">Socials Blogs')
template = template.replace('cat=youtube', 'cat=socials')

cat_map_path = 'c:/Users/Comp/silverbowl/category_map.json'
with open(cat_map_path, 'r', encoding='utf-8') as f:
    cat_map = json.load(f)

if 'youtube' in cat_map:
    cat_map['socials'] = cat_map.pop('youtube')
if 'crypto' not in cat_map:
    cat_map['crypto'] = []

blog_dir = 'c:/Users/Comp/silverbowl/blog'
for title in titles:
    slug = create_slug(title)
    if slug not in cat_map['crypto']:
        cat_map['crypto'].append(slug)
    
    # Extract the article body replacement
    content = generate_article_content(title)
    
    # Use regex to replace the old article content with new
    new_html = re.sub(r'<article class="article-content">.*?</article>', 
                      f'<article class="article-content">\n{content}\n            </article>', 
                      template, flags=re.DOTALL)
    
    # Replace Title and Meta
    new_html = re.sub(r'<title>.*?</title>', f'<title>{title} | GoldenKash</title>', new_html)
    new_html = re.sub(r'<meta name="description"\s+content=".*?" />', f'<meta name="description"\n        content="Discover key insights and trends about {title}. Read our comprehensive guide tailored for 2026." />', new_html)
    new_html = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="https://goldenkash.com/blog/{slug}" />', new_html)
    
    # Replace H1
    new_html = re.sub(r'<h1>.*?</h1>', f'<h1>{title}</h1>', new_html)
    
    # Replace Breadcrumb section
    # <nav class="breadcrumb"><a href="../index.html">Home</a> <span>›</span> <a href="index.html">Blog</a>
    #             <span>›</span> <span>Make Money</span>
    # </nav>
    new_html = re.sub(r'<span>Make Money</span>', '<span>Crypto</span>', new_html)
    
    # Badge
    new_html = re.sub(r'<span class="badge badge-purple" style="margin-bottom:1rem">Side Hustle</span>', '<span class="badge badge-yellow" style="margin-bottom:1rem;background-color:#f5a623;color:#fff;">Crypto Insights</span>', new_html)

    # Sidebar TOC
    toc = """<div class="toc-title">📋 Contents</div>
                    <ol>
                        <li><a href="#key-insights">Key Insights</a></li>
                        <li><a href="#opportunities">Future Opportunities</a></li>
                        <li><a href="#conclusion">Conclusion</a></li>
                    </ol>"""
    new_html = re.sub(r'<div class="toc-title">📋 Contents</div>.*?<div class="sidebar-widget">', toc + '\n                </div>\n                <div class="sidebar-widget">', new_html, flags=re.DOTALL)
    
    with open(os.path.join(blog_dir, slug), 'w', encoding='utf-8') as f:
        f.write(new_html)

# Now update the rest of the HTML files for the socials rename
dir_paths = ['c:/Users/Comp/silverbowl', 'c:/Users/Comp/silverbowl/blog']
for d in dir_paths:
    for f in os.listdir(d):
        if f.endswith('.html'):
            path = os.path.join(d, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # replace href="...cat=youtube">YouTube</a> with href="...cat=socials">Socials Blogs</a>
            content = re.sub(r'cat=youtube">YouTube</a>', 'cat=socials">Socials Blogs</a>', content)
            
            # For breadcrumbs: <span>YouTube</span> when it's just YouTube category
            content = re.sub(r'<span>YouTube</span>', '<span>Socials Blogs</span>', content)
            
            # General cat=youtube to cat=socials
            content = content.replace('cat=youtube', 'cat=socials')

            # Badge inside articles
            content = re.sub(r'<span class="tag">YouTube</span>', '<span class="tag">Socials Blogs</span>', content)

            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

with open(cat_map_path, 'w', encoding='utf-8') as f:
    json.dump(cat_map, f, indent=4)

print("Done generating 15 crypto articles and updating socials!")
