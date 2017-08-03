
from flask import render_template, current_app, Blueprint, redirect, url_for, request, flash, jsonify, session
import json
import os

from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user
from flask_oauthlib.client import OAuth, OAuthException
from webapp.extensions import login_manager, google
from webapp.models.main import User, Post, db
from webapp.forms import UserForm, PostForm
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import configparser
from werkzeug.utils import secure_filename
from docxtpl import DocxTemplate

post_blueprint = Blueprint(
    'post',
    __name__,
    template_folder='../templates/post'
)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def auth_gss_client(path, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name('webapp/auth.json', scopes)
    return gspread.authorize(credentials)

auth_json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'auth.json')
gss_scopes = ['https://spreadsheets.google.com/feeds']
gss_client = auth_gss_client(auth_json_path, gss_scopes)

@post_blueprint.route('/')
def get_index():
    form = PostForm()
    category = request.args.get('category') or 'all'
    if category == 'all':
        posts = Post.query.paginate(per_page=4)
    else:
        posts = Post.query.filter_by(category=category).paginate(per_page=4)
    
    return render_template('posts/index.html', form=form, posts=posts, pagination=posts, endpoint='post.get_index', category=category)

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

    file = request.files['image']
    print('file', request.files)
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    title = request.form.get('title')
    content = request.form.get('content')
    image_path = filename
    category = request.form.get('category')
    post = Post(title, content, image_path, category)
    db.session.add(post)
    db.session.commit()

    # Generate .docx file
    doc = DocxTemplate(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'template.docx'))
    context = { 'title': title, 'content': content, 'updated_at': post.updated_at, 'category': category }
    doc.render(context)
    doc.save(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'uploads/doc_' + str(post.id) + '.docx'))

    # Open spreadsheet and write it
    # sht = gss_client.open_by_key('1FNK3iwe1MLN8xxl4b1_0DMo8xHd_udFOd3VFwm3n2U4')
    # wks = sht.worksheet('posts')
    # cells_list = wks.get_all_records()
    # wks.insert_row([post.id, title, content, category], index=post.id + 1)
    # print(cells_list)

    return redirect(url_for('post.get_post', post_id=post.id))

@post_blueprint.route('/<post_id>/update')
@login_required
def get_update_post(post_id):
    form = PostForm()
    post = Post.query.filter_by(id=post_id).first()

    return render_template('posts/update_post.html', form=form, post=post)

@post_blueprint.route('/<post_id>/update')
@login_required
def post_update_post(post_id):
    form = PostForm()
    file = request.files['image']
    print('file', request.files)
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    title = request.form.get('title')
    content = request.form.get('content')
    image_path = filename
    category = request.form.get('category')

    post = Post.query.filter_by(id=post_id).first()
    post.title = title
    post.content = content
    post.image_path = image_path
    post.category = category
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('post.get_post', post_id=post.id))

@post_blueprint.route('/<post_id>/delete', methods=['POST'])
@login_required
def post_delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('post.get_index'))
