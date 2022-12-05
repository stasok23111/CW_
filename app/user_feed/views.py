from flask import render_template, Blueprint, jsonify, request
from utils.utils import get_posts_by_user

user_feed_blueprint = Blueprint(
    'user_feed_blueprint',
    __name__,
    template_folder='templates')


@user_feed_blueprint.route('/user_feed/<username>', methods=['GET'])
def user_feed_page(username):

    user_posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts= user_posts, username=username)

