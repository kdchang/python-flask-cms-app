from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    google_id = db.Column(db.String(120), unique=True)

    def __init__(self, username, email, google_id):
        self.username = username
        self.email = email
        self.google_id = google_id

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), unique=True)
    content = db.Column(db.String(120), unique=True)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<User %r>' % self.username
