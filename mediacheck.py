import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dateutil.parser import parse as dateparse
import pytz
import json
import os
import requests
import dotenv

# Funkce pro kontrolu, zda článek obsahuje daná klíčová slova
def contains_keywords(text, keywords):
    text = text.lower()
    return any(keyword in text for keyword in keywords)

# Funkce pro získání textu z entry summary
def get_summary_text(entry):
    summary_text = entry.summary if 'summary' in entry else ''
    if '<' in summary_text and '>' in summary_text:  # Kontrola, zda obsahuje HTML značky
        return BeautifulSoup(summary_text, 'html.parser').get_text()
    return summary_text

# Načtení a filtrování článků z RSS kanálů
def fetch_and_filter_rss(feed_url, start_date, end_date):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        article_date = dateparse(entry.published).replace(tzinfo=pytz.UTC)
        if start_date <= article_date <= end_date:
            summary_text = get_summary_text(entry)
            content = entry.title + " " + summary_text
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'content': content
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

# Uložení výsledků filtrování do souboru a jejich zobrazení
def save_and_display_articles(articles, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    display_articles(articles)

# Zobrazení filtrovaných článků
def display_articles(articles):
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print()

# Hlavní program
if __name__ == "__main__":
    # Seznam RSS kanálů

    feeds = [
        'https://hlidacipes.org/feed/',
        'https://www.irozhlas.cz/rss/irozhlas/tag/7708693',
        'https://denikn.cz/minuta/feed/',
        'https://www.mvcr.cz/chh/SCRIPT/rss.aspx?nid='
        'https://cedmohub.eu/cs/feed/',
        'https://europeanvalues.cz/cs/feed/',
        'https://demagog.cz/rss/index.atom',
        'https://www.voxpot.cz/feed/',
        'https://www.aktuality.sk/rss/',
        'https://zpravy.aktualne.cz/rss/',
        'https://www.seznamzpravy.cz/rss',
        'https://www.irozhlas.cz/rss/irozhlas/section/zpravy-domov',
        'https://www.irozhlas.cz/rss/irozhlas/section/zpravy-svet',
        'https://www.lupa.cz/rss/clanky/',
        'https://www.denik.cz/rss/zpravy.html',
        'https://www.novinky.cz/rss',
        'https://euractiv.cz/feed/',
        'https://euractiv.sk/feed/',
        'https://cc.cz/feed/',
        'https://www.ceskenoviny.cz/sluzby/rss/cr.php',
        'https://www.ceskenoviny.cz/sluzby/rss/svet.php',
        'https://www.zive.cz/rss/sc-47/',
        'https://servis.idnes.cz/rss.aspx?c=zpravodaj',
        'https://ct24.ceskatelevize.cz/rss/tema/hlavni-zpravy-84313',
        'https://domaci.hn.cz/?m=rss',
        'https://zahranicni.hn.cz/?m=rss',
        'https://www.investigace.cz/feed/',
        'https://www.sme.sk/rss-title',
        'https://spravy.rtvs.sk/feed/',
        'https://www.respekt.cz/api/rss?type=articles&unlocked=1',
        'https://refresher.cz/rss',
        # Přidejte další RSS kanály podle potřeby
    ]

    # Klíčová slova pro filtrování
    keywords = [
    'dezinforma',
    'misinformace',
    'hoax',
    'fake news',
    'propaganda',
    'dezinformacie',
    'podvod',
    'twitter',
    'facebook',
    'umělá',
    'musk',
    'threads',
    'tik tok',
    'faleš',
    'konspirační',
    'deepfake',
    'manipulace',
    'botnet',
    'ddos',
    'troll',
    'sociální inženýrství',
    'clickbait',
    'kybernetick',
    'sociální sítě',
    'mediální gramotnost',
    'ověřování faktů',
    'řetězový',
    'svoboda slova',
    'fact-checking',
    'faloš',
    'manipulácia',
    'cenzúr',
    'cenzur',
    'algoritmy',
    'overovanie faktov',
    'misinformácie'
    ]

    # Datumové rozmezí (datumy s časovou zónou UTC)
    start_date = datetime(2024, 6, 14, tzinfo=pytz.UTC)
    end_date = datetime(2024, 6, 16, 23, 59, 59, tzinfo=pytz.UTC)

    new_articles = []
    for feed_url in feeds:
        new_articles.extend(fetch_and_filter_rss(feed_url, start_date, end_date))

    # send articles by POST request
    dotenv.load_dotenv()
    post_url = os.getenv('POST_ARTICLES_URL')
    requests.post(post_url, json=new_articles)


    # Název souboru s kompletním obsahem RSS kanálů
    # rss_content_file = "rss-obsah.json"

    # Aktualizace obsahu RSS kanálů ve souboru
    # updated_rss_content = update_rss_content_file(feeds, rss_content_file, start_date, end_date)

    # Filtrování a zobrazení článků s klíčovými slovy
    # filtered_articles = [article for article in updated_rss_content if contains_keywords(article['content'], keywords)]
    
    # Vytvoření názvu souboru pro filtrované články
    # file_name_suffix = start_date.strftime("%d-%m") + "-" + end_date.strftime("%d-%m") + ".json"
    # filtered_articles_file = "filtered_articles_" + file_name_suffix

    # Uložení a zobrazení filtrovaných článků
    # save_and_display_articles(filtered_articles, filtered_articles_file)