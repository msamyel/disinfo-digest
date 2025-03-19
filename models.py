from app import db
from unicodedata import normalize
from string import printable
import re


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    domain = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False, unique=True)
    media_url = db.Column(db.String, nullable=True)
    content = db.Column(db.Text, nullable=True)
    hashtags = db.Column(db.String, nullable=True)
    published_at_cet = db.Column(db.DateTime, nullable=False)
    published_at_cet_str = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    week = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    is_hidden = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Article {self.title}>'

    def uri_title(self):
        no_accents = self.remove_accents(self.title)
        no_spaces = no_accents.replace(' ', '-')
        return self.replace_non_letters(no_spaces)

    @staticmethod
    def remove_accents(data):
        return ''.join(x for x in normalize('NFKD', data) if x in printable).lower()

    @staticmethod
    def replace_non_letters(data):
        pattern = re.compile('^[a-zA-Z0-9-]*$')
        return ''.join(x for x in data if pattern.match(x))

    @staticmethod
    def exclude_hidden():
        # must use == instead of is because of the SQLAlchemy ORM
        return Article.query.filter(Article.is_hidden == False)
