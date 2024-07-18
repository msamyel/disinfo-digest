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
def fetch_and_filter_rss(feed_url, start_date, end_date):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        if not hasattr(entry, 'published'):
            continue  # Přeskočit články bez atributu 'published'
        article_date = dateparse(entry.published).replace(tzinfo=pytz.UTC)
        if start_date <= article_date <= end_date:
            summary_text = get_summary_text(entry)
            content = summary_text
            keyword_found = contains_keywords(content)  # Změna: Uložení nalezeného klíčového slova
            link = entry.link
            source = get_server_name(link)
            if keyword_found or source == 'cedmohub.eu':
                articles.append({
                    'title': entry.title,
                    'link': link,
                    'published': entry.published,
                    'content': summary_text,
                    'source': source,  # Přidání serveru do slovníku
                    'keyword': keyword_found if keyword_found else ''  # Přidání klíčového slova do slovníku
                })
    return articles


# Uložení obsahu RSS kanálů do souboru
def save_rss_content_to_file(rss_content, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(rss_content, f, ensure_ascii=False, indent=4)


# Načtení obsahu RSS kanálů ze souboru
def load_rss_content_from_file(file_name):
    rss_content = []
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            rss_content = json.load(f)
    return rss_content


# Aktualizace obsahu RSS kanálů ve souboru na základě nových dat
def update_rss_content_file(feeds, file_name, start_date, end_date):
    # Načtení existujícího obsahu
    rss_content = load_rss_content_from_file(file_name)

    # Získání nových článků a jejich filtrování
    new_articles = []
    for feed_url in feeds:
        new_articles.extend(fetch_and_filter_rss(feed_url, start_date, end_date))

    # Přidání nových článků k existujícím, pokud ještě nejsou přítomny
    existing_links = {article['link'] for article in rss_content}
    for article in new_articles:
        if article['link'] not in existing_links:
            rss_content.append(article)
            existing_links.add(article['link'])

    # Uložení aktualizovaného obsahu zpět do souboru
    save_rss_content_to_file(rss_content, file_name)

    return rss_content


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


def scrape_feed_to_results(feed_url, start_date, end_date):
    print(f'scraping feed {feed_url} at {time.strftime("%H:%M:%S", time.gmtime())}')
    try:
        results.extend(fetch_and_filter_rss(feed_url, start_date, end_date))
    except Exception as e:
        print(f'error scraping feed {feed_url}: {e}')
    print(f'done scraping feed {feed_url} at {time.strftime("%H:%M:%S", time.gmtime())}')


# Hlavní program
if __name__ == "__main__":
    # Seznam RSS kanálů
    feeds = [
        # Weby s hodnocením A, A-, B+ z https://www.nfnz.cz/rating-medii/
        'https://ct24.ceskatelevize.cz/rss/tema/hlavni-zpravy-84313', # A
        'https://www.ceskenoviny.cz/sluzby/rss/cr.php', # A
        'https://www.ceskenoviny.cz/sluzby/rss/svet.php', # A
        'https://denikn.cz/minuta/feed/', # A
        'https://denikn.cz/rss/', # A
        'https://dennikn.sk/rss/', 
        'https://dennikn.sk/minuta/feed',
        'https://denikreferendum.cz/rss.xml', # A - New
        'https://www.e15.cz/rss', # A - New
        'https://www.forum24.cz/feed', # A - New
        'https://hlidacipes.org/feed/', # A
        'https://domaci.hn.cz/?m=rss', # A
        'https://zahranicni.hn.cz/?m=rss', # A
        'https://www.irozhlas.cz/rss/irozhlas/tag/7708693', # A - Ověřovna (vše)
        'https://www.irozhlas.cz/rss/irozhlas/section/zpravy-domov', # A
        'https://www.irozhlas.cz/rss/irozhlas/section/zpravy-svet', # A
        'https://refresher.cz/rss', # A
        'https://refresher.sk/rss', 
        'https://www.respekt.cz/api/rss?type=articles&unlocked=1', # A
        'https://www.seznamzpravy.cz/rss', # A
        'https://www.voxpot.cz/feed/', # A
        'https://zpravy.aktualne.cz/rss/', # A-
        'https://www.denik.cz/rss/zpravy.html', # A-
        'https://www.reflex.cz/rss', # A-
        'https://servis.idnes.cz/rss.aspx?c=zpravodaj', # B+
        'https://www.novinky.cz/rss', # B+
        'https://servis.lidovky.cz/rss.aspx', # B+
        # SK média
        'https://www.aktuality.sk/rss/',
        'https://www.sme.sk/rss-title',
        'https://www.tyzden.sk/feed/',
        'https://hnonline.sk/feed',
        'http://www.teraz.sk/rss/slovensko.rss',
        'http://www.teraz.sk/rss/zahranicie.rss',
        # 'https://spravy.rtvs.sk/feed/', Odstraněno - přechod na státní STVR
        # Ostatní
        'https://www.mvcr.cz/chh/SCRIPT/rss.aspx?nid=',
        'https://cedmohub.eu/cs/feed/',
        'https://europeanvalues.cz/cs/feed/',
        'https://www.lupa.cz/rss/clanky/',
        'https://euractiv.cz/feed/',
        'https://euractiv.sk/feed/',
        'https://cc.cz/feed/',
        'https://www.zive.cz/rss/sc-47/',
        'https://www.investigace.cz/feed/',
        'https://pepikhipik.com/feed/' # New
        'https://www.wired.cz/atom/feed.xml' # New
        'https://cesti-elfove.cz/feed/' # New (vše)
        # Přidejte další RSS kanály podle potřeby
    ]

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