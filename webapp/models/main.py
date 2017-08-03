from webapp.extensions import db
from flask_login import UserMixin, current_user
import time

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    google_id = db.Column(db.String(120), unique=True)
    updated_at = db.Column(db.DateTime)

    def __init__(self, username, email, password=None, google_id=None, updated_at=None):
        self.username = username
        self.email = email
        self.password = password
        self.google_id = google_id
        if updated_at is None:
            updated_at = time.strftime('%Y-%m-%d %H:%M:%S')
        self.updated_at = updated_at

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text())
    image_path = db.Column(db.String(200))
    category = db.Column(db.String(120))
    updated_at = db.Column(db.DateTime)

    def __init__(self, title, content, image_path, category, updated_at=None):
        self.title = title
        self.content = content
        self.image_path = image_path
        self.category = category
        if updated_at is None:
            updated_at = time.strftime('%Y-%m-%d %H:%M:%S')
        self.updated_at = updated_at

    def __repr__(self):
        return '<Post %r>' % self.title
