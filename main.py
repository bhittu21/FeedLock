import feedparser
from flask import Flask, render_template, request

app = Flask(__name__)

RSS_FEEDS = {
    'Yahoo Finance': 'https://finance.yahoo.com/news/rssindex',
    'Hacker News': 'https://news.ycombinator.com/rss',
    'Wall Street Journal': 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml',
    'CNBC': 'https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15839069'
}

@app.route('/')

def index():
    articles = []
    for source, feed in RSS_FEEDS.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    # Sort by publication date if available
    if articles and len(articles) > 1:
        sortable = [a for a in articles if hasattr(a[1], 'published_parsed') and a[1].published_parsed]
        if sortable and len(sortable) > 1:
            articles = sorted(sortable, key=lambda x: x[1].published_parsed, reverse=True)

    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_articles = len(articles)
    start = (page-1)*per_page
    end = start + per_page
    paginated_articles =  articles[start:end]

    return render_template('index.html', articles=paginated_articles, page=page, total_pages= total_articles // per_page +1)


@app.route('/search')

def search():
    query = request.args.get('query', '').strip()
    
    articles = []
    for source, feed in RSS_FEEDS.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    results = [article for article in articles if query and query.lower() in article[1].title.lower()]
    
    return render_template('search_result.html', articles=results, query=query)


import os

if __name__== '__main__':
    # Get port from environment variable (required for Render.com)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
