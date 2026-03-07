"""
Fix blog/index.html:
1. Filter bar: data-filter="youtube" label "YouTube" → data-filter="socials" label "Social Media"
2. All post cards: data-category="youtube" → data-category="socials"
3. Add 15 crypto article cards before closing </div><!-- /post-grid -->
4. Update hero "70 in-depth" → "86 in-depth"
5. Update meta description count
6. Update sidebar "YouTube & Content" → "Social Media"
"""

PATH = 'c:/Users/Comp/silverbowl/blog/index.html'
with open(PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Filter bar button
html = html.replace(
    '<button class="category-filter-btn" data-filter="youtube">YouTube</button>',
    '<button class="category-filter-btn" data-filter="socials">Social Media</button>'
)

# 2. All card data-category
html = html.replace('data-category="youtube"', 'data-category="socials"')

# 3. Meta/hero count
html = html.replace(
    'Browse all 70 in-depth guides on making money online — affiliate marketing, YouTube, freelancing, e-commerce, AI side hustles, and more.',
    'Browse all 86 in-depth guides on making money online — affiliate marketing, crypto, YouTube, freelancing, e-commerce, AI side hustles, and more.'
)
html = html.replace(
    '70 in-depth, honest guides to help you build real online income — wherever you are in the world.',
    '86 in-depth, honest guides to help you build real online income — wherever you are in the world.'
)

# 4. Sidebar categories list: "YouTube & Content" → "Social Media"
html = html.replace(
    '<li><a href="#">YouTube &amp; Content</a><span class="count">2</span></li>',
    '<li><a href="#">Social Media</a><span class="count">13</span></li>'
)
html = html.replace(
    '<li><a href="#">YouTube & Content</a><span class="count">2</span></li>',
    '<li><a href="#">Social Media</a><span class="count">13</span></li>'
)

# 5. Add Crypto section
crypto_articles = [
    ("top-10-cryptocurrencies-to-watch-in-2026.html", "Top 10 Cryptocurrencies to Watch in 2026", "The definitive list of crypto assets with the best upside in 2026 — from Bitcoin to emerging altcoins."),
    ("beginners-guide-to-crypto-investing-how-to-start-safely.html", "Beginner's Guide to Crypto Investing: How to Start Safely", "Step-by-step guide to buying, storing and managing crypto safely for the first time."),
    ("is-bitcoin-still-worth-buying-expert-insights.html", "Is Bitcoin Still Worth Buying? Expert Insights", "An honest look at Bitcoin's current position, price outlook, and whether it makes sense for new investors."),
    ("ethereum-vs-solana-which-blockchain-wins-in-2026.html", "Ethereum vs. Solana: Which Blockchain Wins in 2026?", "A head-to-head comparison of two dominant blockchains — speed, fees, ecosystem, and investment potential."),
    ("crypto-trading-strategies-that-actually-work.html", "Crypto Trading Strategies That Actually Work", "Proven strategies — from DCA to swing trading — that real crypto traders use to stay profitable."),
    ("how-to-spot-the-next-altcoin-boom.html", "How to Spot the Next Altcoin Boom", "Learn how to identify early-stage altcoins before they explode using on-chain data and social signals."),
    ("the-future-of-defi-opportunities-and-risks.html", "The Future of DeFi: Opportunities and Risks", "Decentralized finance is reshaping banking. Understand the top DeFi protocols, yields, and pitfalls."),
    ("crypto-scams-to-avoid-in-2026.html", "Crypto Scams to Avoid in 2026", "Stay safe online — the most common crypto scams and red flags to watch out for in 2026."),
    ("nfts-explained-are-they-still-relevant.html", "NFTs Explained: Are They Still Relevant?", "A clear-headed look at the current NFT market and where genuine value still exists beyond the hype."),
    ("best-crypto-wallets-for-security-and-ease-of-use.html", "Best Crypto Wallets for Security and Ease of Use", "Hardware vs software wallets compared — the safest options for storing your crypto in 2026."),
    ("how-to-make-passive-income-with-crypto-staking.html", "How to Make Passive Income with Crypto Staking", "Earn rewards by staking your crypto assets — beginner-friendly platforms and realistic yields explained."),
    ("crypto-regulations-in-africa-what-you-need-to-know.html", "Crypto Regulations in Africa: What You Need to Know", "A country-by-country overview of crypto regulation across Africa and how it affects your investments."),
    ("5-ways-to-earn-crypto-without-trading.html", "5 Ways to Earn Crypto Without Trading", "Staking, airdrops, learn-to-earn, freelancing for crypto — make money in crypto without buying dips."),
    ("blockchain-technology-beyond-bitcoin-realworld-uses.html", "Blockchain Technology Beyond Bitcoin: Real‑World Uses", "How blockchain is revolutionizing supply chains, healthcare, government, and finance beyond cryptocurrency."),
    ("crypto-mining-in-2026-still-profitable.html", "Crypto Mining in 2026: Still Profitable?", "An honest breakdown of GPU and ASIC mining profitability, electricity costs, and better alternatives."),
]

crypto_cards_html = '\n'
for slug, title, excerpt in crypto_articles:
    crypto_cards_html += f'''
                    <a href="{slug}" class="card post-card" data-category="crypto">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-yellow" style="background:#f5a623;color:#fff;">Crypto</span><span
                                    class="dot">6 min read</span></div>
                            <h2 class="card-title">{title}</h2>
                            <p class="card-excerpt">{excerpt}</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>
'''

html = html.replace(
    '                </div><!-- /post-grid -->',
    crypto_cards_html + '                </div><!-- /post-grid -->'
)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("blog/index.html updated successfully!")
