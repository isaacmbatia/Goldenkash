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

                    <a href="predict-correct-btts-gg-football.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-red">Football</span><span class="dot">8 min read</span></div>
                            <h2 class="card-title">How to Predict Correct BTTS / GG in Football Betting?</h2>
                            <p class="card-excerpt">Master the strategy of predicting Both Teams to Score (BTTS/GG) in football matches using data.</p>
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

                    <a href="predict-draw-outcomes-football.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-red">Football</span><span class="dot">7 min read</span></div>
                            <h2 class="card-title">How to Predict Draw Outcomes in Football?</h2>
                            <p class="card-excerpt">Learn the statistical markers and tactical situations that make predicting draws highly profitable.</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>

                    <a href="sure-football-predictions.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-red">Football</span><span class="dot">6 min read</span></div>
                            <h2 class="card-title">Where Can I Get Sure Football Predictions?</h2>
                            <p class="card-excerpt">The truth about 'sure fits' and 'fixed matches', and where to find legitimate, data-driven football predictions.</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>

                    <a href="recover-losses-correct-score-betting.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-red">Football</span><span class="dot">8 min read</span></div>
                            <h2 class="card-title">How to Recover Losses After a Losing Streak in Correct Score Betting</h2>
                            <p class="card-excerpt">Psychological and mathematical strategies to recover your betting bankroll after suffering severe losses.</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>

                    <a href="poisson-distribution-correct-score.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-red">Football</span><span class="dot">9 min read</span></div>
                            <h2 class="card-title">How to Apply Poisson Distribution for Correct Score Betting</h2>
                            <p class="card-excerpt">Learn how to use mathematical probability models to predict exact correct scores in football.</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>

                    <a href="best-football-prediction-site-2026.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-red">Football</span><span class="dot">6 min read</span></div>
                            <h2 class="card-title">What is the Best Football Prediction Site in 2026?</h2>
                            <p class="card-excerpt">An honest review of the best free and paid football prediction algorithm sites available to bettors.</p>
                            <span class="card-readmore">Read Guide →</span>
                        </div>
                    </a>

                    <a href="predict-over-under-2-5-goals.html" class="card post-card">
                        <div class="card-body">
                            <div class="card-meta"><span class="badge badge-red">Football</span><span class="dot">7 min read</span></div>
                            <h2 class="card-title">How to Predict Over 2.5 and Under 2.5 Goals in Football Matches</h2>
                            <p class="card-excerpt">Learn the statistical markers and tactical situations that make predicting Over/Under 2.5 goals highly profitable.</p>
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
