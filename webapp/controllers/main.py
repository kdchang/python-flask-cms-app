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

from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user, current_user
from flask_oauthlib.client import OAuth, OAuthException
from webapp.extensions import login_manager, google
from webapp.models.main import User, db

@login_manager.user_loader
def load_user(user_id):
    print('user_id', user_id)
    user = User.query.filter_by(id=user_id).first()
    return user

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

@main_blueprint.route('/')
def index():
    title = 'This is title'
    if 'google_token' in session:
        me = google.get('userinfo')
        # return jsonify({"data": me.data})
        user = User.query.filter_by(google_id=me.data['id']).first()

        print(user)

        if user != None:
            # login_user(user)
            return redirect(url_for('main.index'))
        else:
            new_user = User(me.data['name'], me.data['email'], me.data['id'])
            db.session.add(new_user)
            db.session.commit()

        login_manager.login(user)
        return render_template('main/index.html', title=title)

    return redirect(url_for('main.login'))

@main_blueprint.route('/login')
def login():
    return google.authorize(callback=url_for('main.authorized', _external=True))

@main_blueprint.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('main.index'))

@main_blueprint.route('/login/google_authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    return jsonify({"data": me.data})

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')