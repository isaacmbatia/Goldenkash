import os
import re
import json

BASE = 'c:/Users/Comp/silverbowl'
BLOG = os.path.join(BASE, 'blog')
DOMAIN = 'https://goldenkash.com'

# ─────────────── Article definitions ───────────────
articles = [
    ("Top 10 AI Tools to Make Money Online in 2026",
     "A curated rundown of the AI tools that are actually generating income for creators, freelancers, and entrepreneurs right now.",
     ["key-tools", "income-potential", "getting-started"],
     ["Key AI Tools for Income", "Income Potential Overview", "How to Get Started"],
     [
       "From writing assistants to AI-powered design and video tools, the landscape has never been more rich. We break down the top 10 platforms that are generating real income for everyday users across the globe in 2026.",
       "Depending on which tools you adopt, monthly earnings can range from a few hundred to over $5,000. Content creation AI tools tend to have the fastest payoff — sometimes within weeks of consistent usage.",
       "Start with one tool that aligns with your existing skill set. If you write, begin with an AI writing assistant. If you design, explore Midjourney or Adobe Firefly. Master one before adding more to your stack."
     ]),
    ("Best Free AI Apps for Students and Entrepreneurs",
     "The best zero-cost AI apps that help students ace exams and entrepreneurs grow their businesses without spending a dollar.",
     ["top-free-apps", "for-students", "for-entrepreneurs"],
     ["Top Free AI Apps", "Best Apps for Students", "Best Apps for Entrepreneurs"],
     [
       "You don't need a budget to start leveraging AI. Tools like ChatGPT Free, Gamma for presentations, and Canva AI design are genuinely powerful at zero cost.",
       "Students benefit most from AI research assistants, note-takers like Otter.ai, and tutoring bots that explain concepts in plain language.",
       "Entrepreneurs see the most ROI from free AI tools for customer service, email automation, and social media scheduling."
     ]),
    ("How to Use ChatGPT for Side Hustles",
     "Step-by-step guide to using ChatGPT to power freelancing, blogging, content creation, and other income-generating side hustles.",
     ["content-creation", "freelancing", "automation"],
     ["Content Creation with ChatGPT", "Freelancing with AI", "Automating Workflows"],
     [
       "ChatGPT can draft blog posts, product descriptions, social media captions, and YouTube scripts in minutes. The secret is learning to write effective prompts that produce publish-ready results.",
       "Freelancers are using ChatGPT to turbocharge output — handling more clients, faster, while maintaining quality. Services like copywriting, email marketing, and SEO content are the top earners.",
       "Beyond content, ChatGPT can automate client onboarding, generate proposals, answer FAQs, and draft contracts — making you run like a 5-person team solo."
     ]),
    ("AI vs. Human Jobs: What Skills Still Pay?",
     "An honest look at which jobs AI is replacing, which are thriving, and the human skills that will always command a premium.",
     ["at-risk-jobs", "safe-skills", "future-proof"],
     ["Jobs at Risk from AI", "Skills That Still Pay", "How to Future-Proof Your Career"],
     [
       "Repetitive cognitive tasks — data entry, basic graphic design, transcription, and templated writing — are being automated rapidly. Understanding which roles are vulnerable is the first step to pivoting.",
       "Emotional intelligence, creative direction, strategic thinking, and technical AI management are the skills paying the highest premiums. The more human the skill, the safer it is.",
       "The best career strategy is to become the person who directs AI — a prompt engineer, an AI integrator, or a specialist who uses AI tools to deliver 10x output in your existing field."
     ]),
    ("Best Productivity Apps for Remote Workers",
     "The top apps that help remote workers stay focused, manage time effectively, and collaborate seamlessly from anywhere in the world.",
     ["focus-tools", "collaboration", "time-management"],
     ["Focus and Deep Work Tools", "Collaboration Platforms", "Time Management Apps"],
     [
       "Tools like Notion, Obsidian, and Forest help remote workers structure their day, block distractions, and maintain deep work sessions that are impossible in open-plan offices.",
       "Slack, Linear, and Loom are replacing endless meetings. Async video tools in particular are reducing time-zone friction for global teams dramatically.",
       "Time-blocking apps combined with AI scheduling assistants like Reclaim.ai are helping remote workers accomplish more in fewer hours, leaving room for life outside work."
     ]),
    ("AI Trading Bots: Can They Beat the Market?",
     "A balanced, honest look at AI-powered trading bots — how they work, what they can achieve, and the very real risks involved.",
     ["how-bots-work", "performance", "risks"],
     ["How AI Trading Bots Work", "Performance Reality Check", "Real Risks to Know"],
     [
       "AI trading bots analyze price data, sentiment signals, and on-chain metrics at speeds impossible for humans. They execute trades based on pre-set rules or machine learning pattern recognition.",
       "Most retail-grade AI bots do not consistently beat the market. The best performers typically generate 10–25% annual returns in stable markets — comparable to an index fund, but with far more complexity.",
       "The biggest risks are over-optimization (bots trained to past data failing in new markets), exchange downtime, and API key security. Never risk capital you cannot afford to lose entirely."
     ]),
    ("Top 5 AI Tools for Content Creators",
     "The five AI tools that professional content creators are using daily to script, design, edit, and distribute faster than ever before.",
     ["scripting", "design", "distribution"],
     ["AI Tools for Scripting and Writing", "Visual and Video AI Tools", "Distribution and Scheduling"],
     [
       "Jasper and Claude are the go-to AI writing partners for long-form creators, offering brand voice consistency and SEO optimization built in.",
       "Runway ML for video editing and Midjourney for thumbnails and imagery have cut production time by 60% or more for creators who have integrated them.",
       "Tools like Metricool and Buffer now use AI to recommend optimal posting times, suggest hashtags, and analyze performance — making distribution almost fully automated."
     ]),
    ("How to Automate Your Business with AI",
     "A practical guide to identifying which parts of your business can be automated with AI tools today — and exactly how to do it.",
     ["audit", "tools", "implementation"],
     ["Auditing Your Business for Automation", "Best AI Tools by Business Function", "Implementation Without Tech Skills"],
     [
       "Start with a time audit. Track every repetitive task you or your team performs for one week — those are your automation targets. Common wins include email responses, invoicing, and social posting.",
       "The best AI automation tools by category: Zapier + ChatGPT for workflows, HubSpot AI for CRM, Canva AI for design, and Tidio for customer support chatbots.",
       "You don't need to code. No-code platforms like Make.com (formerly Integromat) let you connect apps and build powerful automations using drag-and-drop interfaces with AI built in."
     ]),
    ("Best Tech Gadgets Under $100 That Save You Money",
     "Smart gadgets that pay for themselves quickly by cutting bills, boosting productivity, or enabling income-generating activities.",
     ["smart-home", "productivity-gear", "roi"],
     ["Smart Home Gadgets That Cut Costs", "Productivity Hardware", "Best ROI Tech Purchases"],
     [
       "Smart plugs, programmable thermostats, and LED smart bulbs routinely cut electricity bills by 15–30% within the first month of use — paying for themselves quickly.",
       "A good USB-C hub, a portable monitor, or a compact mechanical keyboard can transform any laptop into a full workstation — boosting output without a big desk setup.",
       "The best ROI gadget purchases are ones that directly enable income: a ring light for content creation, a quality microphone for podcasting, or a drawing tablet for digital freelancing."
     ]),
    ("AI in Africa: Opportunities for Entrepreneurs",
     "How African entrepreneurs are using AI to build businesses, solve local problems, and compete on the global digital economy.",
     ["local-opportunities", "global-reach", "tools-to-use"],
     ["Local AI Opportunities in Africa", "Going Global with AI", "Best AI Tools for African Entrepreneurs"],
     [
       "From AgriTech AI for smallholder farmers to AI-driven M-Pesa fraud detection, African entrepreneurs are building real, scalable businesses using AI to solve hyper-local problems.",
       "AI lowers the barrier to entry for global freelancing. Kenyan, Nigerian, and South African creators are using AI writing and design tools to compete with agencies in Europe and North America.",
       "Tools like ChatGPT, Canva AI, and Copy.ai all work seamlessly on mobile data connections, making them accessible for entrepreneurs with limited infrastructure — a genuine game-changer."
     ]),
    ("Best AI Side Hustles You Can Start in 2026",
     "The highest-paying AI-powered side hustles available right now — with realistic income ranges and step-by-step starting points.",
     ["top-hustles", "income-ranges", "how-to-start"],
     ["Top AI Side Hustles Ranked", "Realistic Income Ranges", "How to Start in 7 Days"],
     [
       "AI content creation, AI image selling, ChatGPT prompt engineering, AI-powered SEO, and AI voice-over work are the top five side hustles generating the most consistent income for beginners.",
       "Entry-level AI side hustlers typically earn $200–$600/month in the first three months. Within 6–12 months, the median rises to $800–$2,500/month with consistent effort.",
       "Day 1–2: Choose your hustle and set up accounts. Day 3–4: Complete your first sample project. Day 5–7: Publish or pitch to your first clients. Most hustles generate the first payment within 30 days."
     ]),
    ("Top 10 Free AI Tools for Small Businesses",
     "Ten AI tools with generous free tiers that small businesses are using to punch above their weight against larger competitors.",
     ["marketing", "operations", "customer-service"],
     ["Free AI Tools for Marketing", "Operations and Workflow AI", "Customer Service AI"],
     [
       "Canva's AI features, Meta's AI creative tools, and Google's Gemini are transforming small business marketing — allowing one-person shops to produce agency-quality content for free.",
       "Trello AI, Notion AI, and Zapier's free tier are automating project management, meeting notes, and repetitive workflows for small teams at zero cost.",
       "Tidio's free chatbot plan handles unlimited conversations on your website, acting as a 24/7 customer service agent that never takes a day off."
     ]),
    ("How to Use AI to Automate Social Media Posts",
     "A complete system for using AI tools to plan, write, design, and schedule social media content — saving 10+ hours per week.",
     ["content-planning", "creation", "scheduling"],
     ["AI-Powered Content Planning", "Creating Posts with AI", "Automated Scheduling"],
     [
       "Start with a monthly content calendar built in ChatGPT or Claude. Prompt it with your niche, goals, and audience, and it will generate a month of post ideas in minutes.",
       "Use Canva AI for graphics, CapCut AI for short-form videos, and ChatGPT for captions. A full week of social media content can be produced in under two hours using this stack.",
       "Buffer and Metricool both offer AI-assisted scheduling that analyzes your audience's peak activity times and posts automatically — no daily check-ins required."
     ]),
    ("AI Tools for Students: Boost Grades and Productivity",
     "The best AI tools that help students research smarter, write better, manage time, and stay ahead without burning out.",
     ["research", "writing", "time-management"],
     ["AI for Academic Research", "AI Writing Assistance", "Time and Focus Management"],
     [
       "Perplexity AI and Elicit are the two best research tools for students — both cite sources, summarize papers, and help build arguments in a fraction of the time of traditional research.",
       "Grammarly AI and QuillBot help students improve drafts, correct grammar, and rephrase complex ideas clearly. Both have free tiers sufficient for most academic work.",
       "Sunsama and Motion use AI to schedule study sessions, balance deadlines, and protect your rest time — the closest thing to having a personal academic coach."
     ]),
    ("Best AI Apps for Content Creation and Blogging",
     "The AI-powered apps that bloggers and content creators are relying on to research, write, optimise and publish faster than ever.",
     ["research", "writing", "seo"],
     ["AI Research Tools for Bloggers", "Writing and Editing with AI", "SEO Optimization with AI"],
     [
       "Perplexity for research, Frase for SEO briefs, and SurferSEO for optimization are the three most impactful AI tools for a content-focused workflow.",
       "Jasper and Claude excel at long-form blog posts. With the right prompts and a clear outline, a full 2,000-word article can be drafted, edited, and ready to publish in under 45 minutes.",
       "Rank Math's AI and Clearscope help bloggers optimize every post for search intent, keyword density, and readability before hitting publish — giving a significant edge in organic rankings."
     ]),
]

# ─────────────── Read template ───────────────────
with open(os.path.join(BLOG, 'watch-videos-earn-money.html'), 'r', encoding='utf-8') as f:
    TEMPLATE = f.read()

# Apply global socials fix to template just in case
TEMPLATE = TEMPLATE.replace('cat=youtube', 'cat=socials').replace('>YouTube<', '>Social Media<')

def slugify(title):
    s = title.lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s).strip('-')
    return s + '.html'

# ─────────────── Generate articles ───────────────
new_slugs = []
for title, meta_desc, section_ids, section_titles, section_bodies in articles:
    slug = slugify(title)
    new_slugs.append(slug)

    # Build article body
    sections_html = ''
    for sid, stitle, sbody in zip(section_ids, section_titles, section_bodies):
        sections_html += f'\n                <h2 id="{sid}">{stitle}</h2>\n                <p>{sbody}</p>\n'

    article_body = f'''\n                <p>Welcome to our in-depth guide on <strong>{title}</strong>. In 2026, AI and technology are the single biggest factors shaping how people earn, work, and live online.</p>
                <p>Whether you're a student, entrepreneur, content creator, or remote worker, this guide covers exactly what you need to know to get ahead of the curve.</p>
                {sections_html}
                <h2>Other Ways to Make Money</h2>
                <ul>
                    <li><strong><a href="ai-tools-make-money.html">How to Use AI Tools to Make Money Online</a></strong></li>
                    <li><strong><a href="ai-side-hustles-2026.html">Best AI Side Hustles for Beginners in 2026</a></strong></li>
                    <li><strong><a href="affiliate-marketing-beginners.html">Affiliate Marketing for Beginners</a></strong></li>
                </ul>
                <div class="share-bar"><span>Share:</span><a class="share-btn share-tw" href="#" target="_blank">Twitter</a><a class="share-btn share-wa" href="#" target="_blank">WhatsApp</a></div>
                <div class="tags-row"><span class="tag">Tech</span><span class="tag">AI</span><span class="tag">2026</span></div>'''

    # TOC
    toc_items = ''.join(f'<li><a href="#{sid}">{stitle}</a></li>' for sid, stitle in zip(section_ids, section_titles))

    html = TEMPLATE

    # Meta
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | GoldenKash</title>', html)
    html = re.sub(r'<meta name="description"\s+content=".*?" />', f'<meta name="description"\n        content="{meta_desc}" />', html, flags=re.DOTALL)
    html = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="{DOMAIN}/blog/{slug}" />', html)

    # Hero
    html = re.sub(r'<h1>.*?</h1>', f'<h1>{title}</h1>', html)
    html = re.sub(r'<span>Make Money</span>', '<span>Tech &amp; AI</span>', html)
    html = html.replace(
        '<span class="badge badge-purple" style="margin-bottom:1rem">Side Hustle</span>',
        '<span class="badge badge-blue" style="margin-bottom:1rem">Tech &amp; AI</span>'
    )

    # Article content
    html = re.sub(r'<article class="article-content">.*?</article>', f'<article class="article-content">{article_body}\n            </article>', html, flags=re.DOTALL)

    # TOC sidebar
    html = re.sub(
        r'<div class="toc-title">📋 Contents</div>.*?</ol>',
        f'<div class="toc-title">📋 Contents</div>\n                    <ol>{toc_items}</ol>',
        html, flags=re.DOTALL
    )

    out = os.path.join(BLOG, slug)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Generated {len(new_slugs)} Tech & AI articles.")

# ─────────────── Update category_map.json ────────
cat_map_path = os.path.join(BASE, 'category_map.json')
with open(cat_map_path, 'r', encoding='utf-8') as f:
    cat_map = json.load(f)

cat_map['techai'] = new_slugs

with open(cat_map_path, 'w', encoding='utf-8') as f:
    json.dump(cat_map, f, indent=4)
print("category_map.json updated.")

# ─────────────── Update nav in all HTML files ────
NAV_INSERT = '<li><a href="{prefix}index.html?cat=techai">Tech &amp; AI</a></li>'
NAV_MARKER_ROOT  = '<li><a href="blog/index.html?cat=tools">Tools</a></li>'
NAV_MARKER_BLOG  = '<li><a href="index.html?cat=tools">Tools</a></li>'

dirs = [BASE, BLOG, os.path.join(BASE, '_includes')]
nav_changed = 0
for d in dirs:
    if not os.path.isdir(d):
        continue
    for fname in os.listdir(d):
        if not fname.endswith('.html'):
            continue
        path = os.path.join(d, fname)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'cat=techai' in content:  # already updated
            continue

        updated = content
        # root-level pages
        if NAV_MARKER_ROOT in updated:
            updated = updated.replace(NAV_MARKER_ROOT,
                NAV_MARKER_ROOT + '\n                ' + NAV_INSERT.format(prefix='blog/'))
        # blog-level pages
        if NAV_MARKER_BLOG in updated:
            updated = updated.replace(NAV_MARKER_BLOG,
                NAV_MARKER_BLOG + '\n                ' + NAV_INSERT.format(prefix=''))

        if updated != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(updated)
            nav_changed += 1

print(f"Nav updated in {nav_changed} files.")

# ─────────────── Update blog/index.html ──────────
blog_index = os.path.join(BLOG, 'index.html')
with open(blog_index, 'r', encoding='utf-8') as f:
    bi = f.read()

# 1. Filter bar – insert after tools button
TOOLS_BTN = '<button class="category-filter-btn" data-filter="tools">Tools</button>'
TECHAI_BTN = '<button class="category-filter-btn" data-filter="techai">Tech &amp; AI</button>'
if TECHAI_BTN not in bi:
    bi = bi.replace(TOOLS_BTN, TOOLS_BTN + '\n            ' + TECHAI_BTN)

# 2. Guide count: 86 → 101
bi = bi.replace('86 in-depth, honest guides', '101 in-depth, honest guides')
bi = bi.replace('Browse all 86 in-depth guides', 'Browse all 101 in-depth guides')

# 3. Build and inject cards
article_titles = [a[0] for a in articles]
article_excerpts = [a[1] for a in articles]
cards_html = '\n'
for i, slug in enumerate(new_slugs):
    title = article_titles[i]
    excerpt = article_excerpts[i]
    cards_html += f'''
                    <a href="{slug}" class="card post-card" data-category="techai">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-blue">Tech &amp; AI</span><span class="dot">7 min read</span></div>
                            <h2 class="card-title">{title}</h2>
                            <p class="card-excerpt">{excerpt}</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>
'''

bi = bi.replace('                </div><!-- /post-grid -->', cards_html + '                </div><!-- /post-grid -->')

with open(blog_index, 'w', encoding='utf-8') as f:
    f.write(bi)
print("blog/index.html updated.")

# ─────────────── Update index.html homepage ──────
homepage = os.path.join(BASE, 'index.html')
with open(homepage, 'r', encoding='utf-8') as f:
    hp = f.read()

# Category card – insert before closing </div> of cat-grid
CAT_CARD = '''
                <a href="blog/index.html?cat=techai" class="cat-card">
                    <div class="cat-icon">🤖</div>
                    <h4>Tech &amp; AI</h4>
                    <p>AI tools, productivity apps, and tech side hustles</p>
                    <span class="cat-count">15+ guides</span>
                </a>'''

# Insert before the closing tag of cat-grid
hp = hp.replace('            </div>\n        </div>\n    </section>\n\n    <!-- ═══════════════════════════════════════════════════════════\n     EMAIL OPT-IN',
    CAT_CARD + '\n            </div>\n        </div>\n    </section>\n\n    <!-- ═══════════════════════════════════════════════════════════\n     EMAIL OPT-IN')

# Update guide counts
hp = hp.replace('70+\u003c/span\u003e\u003cspan class=\"stat-label\"\u003eIn-Depth Guides', '100+</span><span class="stat-label">In-Depth Guides')
hp = hp.replace('<span class="stat-num">70+</span><span class="stat-label">In-Depth Guides', '<span class="stat-num">100+</span><span class="stat-label">In-Depth Guides')

with open(homepage, 'w', encoding='utf-8') as f:
    f.write(hp)
print("index.html homepage updated.")

# ─────────────── Rebuild sitemap.xml ─────────────
import glob
blog_files = sorted(os.path.basename(f) for f in glob.glob(os.path.join(BLOG, '*.html')) if not f.endswith('index.html'))
lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    '  <!-- Main Pages -->'
]
for path, pri, freq in [('', '1.0', 'weekly'), ('start-here.html', '0.9', 'monthly'),
                        ('blog/index.html', '0.9', 'daily'), ('resources.html', '0.8', 'monthly'),
                        ('about.html', '0.5', 'yearly'), ('contact.html', '0.4', 'yearly')]:
    url = f'{DOMAIN}/{path}' if path else f'{DOMAIN}/'
    lines.append(f'  <url><loc>{url}</loc><changefreq>{freq}</changefreq><priority>{pri}</priority></url>')
lines.append('  <!-- Blog Articles -->')
for fname in blog_files:
    lines.append(f'  <url><loc>{DOMAIN}/blog/{fname}</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>')
lines.append('</urlset>')
with open(os.path.join(BASE, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print(f"sitemap.xml rebuilt with {len(blog_files)} blog URLs.")
print("ALL DONE.")
