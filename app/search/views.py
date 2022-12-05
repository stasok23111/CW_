from flask import render_template, Blueprint, request
from utils.utils import search_for_posts, get_posts_by_user

search_blueprint = Blueprint(
    'search_blueprint',
    __name__,
    template_folder='templates')


@search_blueprint.route('/search/')
def search_index():
    s = request.args.get('s', '')
    posts = search_for_posts(s)
    len_posts = len(posts)
    return render_template('search.html', s=s, posts=posts, len_posts=len_posts)




