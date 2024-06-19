from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from config import Config
from urllib.parse import urlparse
from flask import request, render_template
import dateutil.parser
import pytz
from flask_moment import Moment


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# js library for localizing time
moment = Moment(app)

from models import *

@app.route("/")
def index():
    articles = Article.query.order_by(Article.published_at.desc()).limit(15)
    return render_template(
        'index.html',
        title='Home',
        articles=articles,
        article_counts=get_article_counts())


@app.route("/date/<int:year>-<int:month>-<int:day>")
def index_filtered_by_date(year, month, day):
    date = f"{year}-{month:02d}-{day:02d}"
    articles = Article.query.filter(sa.func.strftime("%Y-%m-%d", Article.published_at) == date).all()
    return render_template(
        'index.html',
        title=date,
        date=date,
        articles=articles,
        article_counts=get_article_counts())


def get_article_counts():
    article_counts = (db.session
                      .query(
        sa.func.strftime("%Y-%m-%d", Article.published_at).label('date'),
        sa.func.count(Article.id).label('count'))
                      .group_by(sa.func.strftime("%Y-%m-%d", Article.published_at))
                      .all())
    return article_counts

@app.route("/articles", methods=['POST'])
def save_articles():
    rss_content = request.get_json()
    # insert row with sqlalchemy
    for article in rss_content:
        parsed_uri = urlparse(article['link'])
        domain = '{uri.netloc}'.format(uri=parsed_uri)

        date = dateutil.parser.parse(article['published'])
        date = date.replace(tzinfo=pytz.UTC)
        utc_date = date.astimezone(pytz.UTC)
        year, week_number, _ = utc_date.isocalendar()

        new_article = Article(
            title=article['title'],
            domain=domain,
            url=article['link'],
            content=article['content'],
            published_at=utc_date,
            year=year,
            week=week_number
        )
        db.session.add(new_article)
    db.session.commit()
    return "Articles saved!"


@app.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()
    print("Database initialized!")
