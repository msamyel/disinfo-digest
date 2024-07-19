import feedparser
import time
import requests
import concurrent.futures
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dateutil.parser import parse as dateparse
import pytz
import json
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from keywords import KEYWORDS_SEARCH_TABLE as KEYWORDS
from classes.rss_feed import RssFeed

NUM_THREADS = 5
results = []
load_dotenv()


# Funkce pro kontrolu, zda článek obsahuje daná klíčová slova
def contains_keywords(text):
    text = text.lower()
    for key, full_word in KEYWORDS.items():
        if key in text:
            return full_word
    return None


# Funkce pro získání textu z entry summary
def get_summary_text(entry):
    summary_text = entry.summary if 'summary' in entry else ''
    if '<' in summary_text and '>' in summary_text:  # Kontrola, zda obsahuje HTML značky
        return BeautifulSoup(summary_text, 'html.parser').get_text()
    return summary_text


# Funkce pro získání názvu serveru z URL (bez 'www.')
def get_server_name(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc
    if netloc.startswith('www.'):
        netloc = netloc[4:]
    return netloc


# Načtení a filtrování článků z RSS kanálů
def fetch_and_filter_rss(feed: RssFeed, start_date, end_date):
    articles = []
    feed_content = feedparser.parse(feed.url)
    for entry in feed_content.entries:
        if not hasattr(entry, 'published'):
            continue  # Přeskočit články bez atributu 'published'
        article_date = dateparse(entry.published).replace(tzinfo=pytz.UTC)
        if start_date <= article_date <= end_date:
            summary_text = get_summary_text(entry)
            content = summary_text
            keyword_found = feed.tag_to_enforce or contains_keywords(content)
            link = entry.link
            source = get_server_name(link)
            if feed.save_all_articles or keyword_found:
                articles.append({
                    'title': entry.title,
                    'link': link,
                    'published': entry.published,
                    'content': summary_text,
                    'source': source,  # Přidání serveru do slovníku
                    'keyword': keyword_found  # Přidání klíčového slova do slovníku
                })
    return articles


# Zobrazení filtrovaných článků na obrazovku
def display_articles_to_console(articles):
    for article in articles:
        source = article.get('source', 'unknown')  # Zajištění, že klíč 'source' vždy existuje
        keyword = article.get('keyword', 'N/A')  # Zajištění, že klíč 'keyword' vždy existuje
        published_date = dateparse(article['published']).strftime("%d.%m")
        line = f"- {article['title']} ({source}, {published_date} - {keyword})"
        print(line)


# Uložení filtrovaných článků do souboru monitoring.md
def save_articles_to_file(articles, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for article in articles:
            source = article.get('source', 'unknown')  # Zajištění, že klíč 'source' vždy existuje
            keyword = article.get('keyword', 'N/A')  # Zajištění, že klíč 'keyword' vždy existuje
            published_date = dateparse(article['published']).strftime("%d.%m")
            line = f'<li class="novinka" data-keywords="{keyword}"><a href="{article["link"]}" target="_blank">{article["title"]}</a> <small>({source})</small> <code class="highlighter-rouge">{keyword}</code></li>\n'
            f.write(line)


def scrape_feed_to_results(feed: RssFeed, start_date, end_date):
    print(f'scraping feed {feed.url} at {time.strftime("%H:%M:%S", time.gmtime())}')
    try:
        results.extend(fetch_and_filter_rss(feed, start_date, end_date))
    except Exception as e:
        print(f'error scraping feed {feed.url}: {e})')
    print(f'done scraping feed {feed.url} at {time.strftime("%H:%M:%S", time.gmtime())}')


# Hlavní program
if __name__ == "__main__":
    # Seznam RSS kanálů
    feeds = []
    feeds.append(RssFeed('https://ct24.ceskatelevize.cz/rss/tema/hlavni-zpravy-84313')),  # A
    feeds.append(RssFeed('https://www.ceskenoviny.cz/sluzby/rss/cr.php')),  # A
    feeds.append(RssFeed('https://www.ceskenoviny.cz/sluzby/rss/svet.php')),  # A
    feeds.append(RssFeed('https://denikn.cz/minuta/feed/')),  # A
    feeds.append(RssFeed('https://denikn.cz/rss/')),  # A
    feeds.append(RssFeed('https://dennikn.sk/rss/')),
    feeds.append(RssFeed('https://dennikn.sk/minuta/feed')),
    feeds.append(RssFeed('https://denikreferendum.cz/rss.xml')),  # A - New
    feeds.append(RssFeed('https://www.e15.cz/rss')),  # A - New
    feeds.append(RssFeed('https://hlidacipes.org/feed/')),  # A
    feeds.append(RssFeed('https://domaci.hn.cz/?m=rss')),  # A
    feeds.append(RssFeed('https://zahranicni.hn.cz/?m=rss')),  # A
    feeds.append(RssFeed('https://www.irozhlas.cz/rss/irozhlas/tag/7708693',
                         save_all_articles=True,
                         tag_to_enforce='fact-checking')),  # A - Ověřovna (vše)
    feeds.append(RssFeed('https://www.irozhlas.cz/rss/irozhlas/section/zpravy-domov')),  # A
    feeds.append(RssFeed('https://www.irozhlas.cz/rss/irozhlas/section/zpravy-svet')),  # A
    feeds.append(RssFeed('https://refresher.cz/rss')),  # A
    feeds.append(RssFeed('https://refresher.sk/rss')),
    feeds.append(RssFeed('https://www.respekt.cz/api/rss?type=articles&unlocked=1')),  # A
    feeds.append(RssFeed('https://www.seznamzpravy.cz/rss')),  # A
    feeds.append(RssFeed('https://www.voxpot.cz/feed/')),  # A
    feeds.append(RssFeed('https://zpravy.aktualne.cz/rss/')),  # A-
    feeds.append(RssFeed('https://www.denik.cz/rss/zpravy.html')),  # A-
    feeds.append(RssFeed('https://www.reflex.cz/rss')),  # A-
    feeds.append(RssFeed('https://servis.idnes.cz/rss.aspx?c=zpravodaj', ))  # B+
    feeds.append(RssFeed('https://www.novinky.cz/rss')),  # B+
    feeds.append(RssFeed('https://servis.lidovky.cz/rss.aspx')),  # B+
    # SK média
    feeds.append(RssFeed('https://www.aktuality.sk/rss/')),
    feeds.append(RssFeed('https://www.sme.sk/rss-title')),
    feeds.append(RssFeed('https://www.tyzden.sk/feed/')),
    feeds.append(RssFeed('https://hnonline.sk/feed')),
    feeds.append(RssFeed('http://www.teraz.sk/rss/slovensko.rss')),
    feeds.append(RssFeed('http://www.teraz.sk/rss/zahranicie.rss')),
    # 'https://spravy.rtvs.sk/feed/', Odstraněno - přechod na státní STVR
    # Ostatní
    feeds.append(RssFeed('https://www.mvcr.cz/chh/SCRIPT/rss.aspx?nid=')),
    feeds.append(RssFeed('https://cedmohub.eu/cs/feed/',
                         save_all_articles=True)),
    feeds.append(RssFeed('https://europeanvalues.cz/cs/feed/')),
    feeds.append(RssFeed('https://www.lupa.cz/rss/clanky/')),
    feeds.append(RssFeed('https://euractiv.cz/feed/')),
    feeds.append(RssFeed('https://euractiv.sk/feed/')),
    feeds.append(RssFeed('https://cc.cz/feed/')),
    feeds.append(RssFeed('https://www.zive.cz/rss/sc-47/')),
    feeds.append(RssFeed('https://www.investigace.cz/feed/')),
    feeds.append(RssFeed('https://pepikhipik.com/feed/')),  # New
    feeds.append(RssFeed('https://www.wired.cz/atom/feed.xml')),  # New
    feeds.append(RssFeed('https://cesti-elfove.cz/feed/',
                         save_all_articles=True,
                         tag_to_enforce='fact-checking')),  # New (vše)
    # Přidejte další RSS kanály podle potřeby

    # Datumové rozmezí (datumy s časovou zónou UTC)
    now = datetime.now().astimezone(pytz.UTC)
    start_date = now - timedelta(hours=4)
    end_date = now

    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        executor.map(
            scrape_feed_to_results,
            feeds,
            [start_date] * len(feeds),
            [end_date] * len(feeds))

    filtered_articles = [
        article for article in results
        if contains_keywords(article['content']) and
           start_date <= dateparse(article['published']).replace(tzinfo=pytz.UTC) <= end_date
    ]

    post_url = os.getenv('POST_ARTICLES_URL')
    api_secret = os.getenv('API_SECRET')
    res = requests.post(post_url, json=filtered_articles, headers={'X-Api-Key': api_secret})
    print(res.status_code, res.content)
