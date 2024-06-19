from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
    articles = Article.query.order_by(Article.published_at.desc()).all()
    return render_template('index.html', title='Home', articles=articles)


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
