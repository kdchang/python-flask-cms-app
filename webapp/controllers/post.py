
from flask import render_template, current_app, Blueprint, redirect, url_for, request, flash, jsonify, session
import json
import os

from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from flask_oauthlib.client import OAuth, OAuthException
from webapp.extensions import login_manager, google
from webapp.models.main import User, Post, db
from webapp.forms import UserForm, PostForm
import gspread

post_blueprint = Blueprint(
    'post',
    __name__,
    template_folder='../templates/post'
)

@post_blueprint.route('/')
def get_index():
    form = PostForm()
    return render_template('posts/index.html', form=form)

@post_blueprint.route('/<post_id>')
def get_post(post_id):
    form = PostForm()
    post = Post.query.filter_by(id=post_id).first()
    return render_template('posts/post.html', form=form, post=post)

@post_blueprint.route('/create')
def get_create_post():
    form = PostForm()
    return render_template('posts/create_post.html', form=form)

@post_blueprint.route('/create', methods=['POST'])
def post_create_post():
    form = PostForm()
    title = request.form.get('title')
    content = request.form.get('content')
    category = request.form.get('category')
    post = Post(title, content, category)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('post.get_post', post_id=post.id))

@post_blueprint.route('/<post_id>/update')
def get_update_post():
    form = PostForm()
    return render_template('posts/create_post.html', form=form)

@post_blueprint.route('/<post_id>/update')
def post_update_post(post_id):
    form = PostForm()
    title = request.form.get('title')
    content = request.form.get('content')
    category = request.form.get('category')
    post = Post.query.filter_by(id=post_id).first()
    post.title = title
    post.content = content
    post.category = category
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('post.get_post'))
