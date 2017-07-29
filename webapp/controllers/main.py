from flask import (
        render_template,
        current_app,
        Blueprint,
        redirect,
        url_for,
        request,
        flash,
        jsonify,
        session
)

import json
import os

from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from flask_oauthlib.client import OAuth, OAuthException
from webapp.extensions import login_manager, google, db
from webapp.models.main import User, Post 
from webapp.forms import UserForm

import gspread
import webapp

@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

@main_blueprint.route('/')
def get_index():
    form = UserForm()
    title = 'This is title'
    posts = Post.query.all()
    return render_template('main/index.html', title=title, form=form, posts=posts)

@main_blueprint.route('/login')
def get_login():
    form = UserForm()
    return render_template('main/login.html', form=form)

@main_blueprint.route('/google_login')
def post_google_login():
    return google.authorize(callback=url_for('main.authorized', _external=True))

@main_blueprint.route('/logout', methods=['POST'])
def post_logout():
    user_id = session['user_id']
    logout_user()
    return redirect(url_for('main.get_index'))

@main_blueprint.route('/login/google_authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return redirect(url_for('main.get_login'))
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    user = User.query.filter_by(google_id=me.data['id']).first()
    if user != None:
        login_user(user)
        session['user_id'] = user.id
        return redirect(url_for('main.get_index'))

    else:
        new_user = User(me.data['name'], me.data['email'], me.data['id'])
        db.session.add(new_user)
        db.session.commit()
        login_user(user)
        session['user_id'] = user.id

    return redirect(url_for('main.get_index'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')