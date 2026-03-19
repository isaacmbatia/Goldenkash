import os

filepath = r'c:\Users\Comp\silverbowl\blog\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_cards = """
                    <a href="watch-videos-earn-money.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-purple">Side Hustle</span><span class="dot">6 min read</span></div>
                            <h2 class="card-title">Watch Videos and Earn Real Money Online: The Ultimate Guide</h2>
                            <p class="card-excerpt">Discover legitimate websites and apps that pay you real money to watch videos, movie trailers, and ads online.</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>

                    <a href="easiest-way-make-money-online.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-green">Beginner</span><span class="dot">7 min read</span></div>
                            <h2 class="card-title">What's the Easiest Way to Make Money Online in 2026?</h2>
                            <p class="card-excerpt">Looking for the absolute easiest ways to make money online with zero experience? We break down the top beginner-friendly hustles.</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>
"""

if '<div class="post-grid">' in content:
    final_content = content.replace('<div class="post-grid">', '<div class="post-grid">\n' + new_cards)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Insertion complete.")
else:
    print("Could not find <div class=\"post-grid\">")
