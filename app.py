from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from config import Config
from urllib.parse import urlparse
from flask import request, render_template
import dateutil.parser
import datetime
import pytz
from flask_moment import Moment
from flask_caching import Cache

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# js library for localizing time
moment = Moment(app)
cache = Cache(app)

from models import *

@app.route("/")
def index():
    search_query = request.args.get('search_query')
    search_from = request.args.get('search_from')
    search_until = request.args.get('search_until')

    if search_from or search_until or search_query:
        articles = get_filtered_articles(search_query, search_from, search_until)
        is_search = True
    else:
        articles = get_newest_articles()
        is_search = False

    return render_template(
        'index.html',
        articles=articles,
        article_counts=get_article_counts(),
        is_search=is_search,
        search_query=search_query,
        search_from=search_from,
        search_until=search_until)


def get_newest_articles():
    now = datetime.datetime.now().astimezone(pytz.timezone("CET")).replace(tzinfo=None)
    week_ago = now - datetime.timedelta(days=7)
    return (Article.exclude_hidden()
            .filter(Article.published_at_cet >= week_ago)
            .order_by(Article.published_at_cet_str.desc(), Article.id.desc())
            .all())


def get_filtered_articles(search_query, start_at, end_at):
    articles = Article.exclude_hidden().order_by(Article.published_at_cet_str.desc(), Article.id.desc())
    if search_query:
        articles = articles.filter(
            sa.or_(
                Article.content.contains(search_query),
                Article.title.contains(search_query)
            )
        )
    if start_at:
        articles = articles.filter(Article.published_at_cet >= start_at)
    if end_at:
        articles = articles.filter(Article.published_at_cet <= end_at)
    return articles.all()


@app.route("/date/<int:year>-<int:month>-<int:day>")
def index_filtered_by_date(year, month, day):
    # get isoweek from month and day
    date = dateutil.parser.parse(f'{year}-{month}-{day}')
    year, week_number, week_day = date.isocalendar()
    start_day, end_day = get_start_and_end_date_from_calendar_week(year, week_number)

    date = f"{year}-{month:02d}-{day:02d}"
    articles = (Article.exclude_hidden()
                .filter(Article.week == week_number, Article.year == year)
                .order_by(Article.published_at_cet.desc(), Article.id.desc())
                .all())
    return render_template(
        'index.html',
        title=f'{day}.{month}. {year}',
        date=date,
        articles=articles,
        article_counts=get_article_counts(),
        year=year,
        week=week_number,
        start_day=start_day,
        end_day=end_day
    )


def get_start_and_end_date_from_calendar_week(year, calendar_week):
    monday = datetime.datetime.strptime(f'{year}-{calendar_week}-1', "%Y-%W-%w").date()
    return monday, monday + datetime.timedelta(days=6.9)


@cache.cached(timeout=7200, key_prefix='article_counts')
def get_article_counts():
    article_counts = (db.session
                      .query(
        Article.published_at_cet_str.label('date'),
        sa.func.count(Article.id).label('count'))
                      .filter(Article.is_hidden == False)
                      .group_by(Article.published_at_cet_str)
                      .all())
    return article_counts

@app.route("/articles", methods=['POST'])
def save_articles():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != app.config['API_SECRET']:
        return "ERROR: Unauthorized", 401

    rss_content = request.get_json()
    for article in rss_content:
        parsed_uri = urlparse(article['link'])
        domain = article['source']
        hashtags = article['keyword']

        date = dateutil.parser.parse(article['published'])
        date_cet = date.astimezone(pytz.timezone("CET"))
        date_cet_timezoneless = date_cet.replace(tzinfo=None)
        year, week_number, day = date_cet_timezoneless.isocalendar()
        date_cet_str = date_cet_timezoneless.strftime("%Y-%m-%d")

        existing_article = Article.query.filter_by(url=article['link']).first()
        if existing_article:
            continue

        new_article = Article(
            title=article['title'],
            domain=domain,
            hashtags=hashtags,
            url=article['link'],
            content=article['content'],
            published_at_cet=date_cet_timezoneless,
            published_at_cet_str=date_cet_str,
            year=year,
            week=week_number,
            day=day,
            is_hidden=False
        )
        db.session.add(new_article)
    db.session.commit()
    return "Articles saved!", 200


@app.route("/articles/hide", methods=['POST'])
def hide_articles():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != app.config['API_SECRET']:
        return "ERROR: Unauthorized", 401

    urls_to_hide = request.get_json()
    for url in urls_to_hide:
        article = Article.query.filter_by(url=url).first()
        if article:
            article.is_hidden = True
            db.session.add(article)

    db.session.commit()
    return "ok", 200

@app.route("/changelog")
def changelog():
    return render_template('changelog.html', title='Changelog')


@app.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()
    print("Database initialized!")
