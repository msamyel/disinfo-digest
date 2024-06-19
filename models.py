from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    domain = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    media_url = db.Column(db.String, nullable=True)
    content = db.Column(db.Text, nullable=True)
    hashtags = db.Column(db.String, nullable=True)
    published_at = db.Column(db.DateTime, server_default=db.func.now())
    year = db.Column(db.Integer, nullable=False)
    week = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'