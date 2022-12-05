from flask import render_template, Blueprint, jsonify, request

from utils.utils import get_comments_by_post_id, get_all_posts, search_for_posts




posts_file = 'data/posts.json'

main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    template_folder='templates')


@main_blueprint.route('/')
def page_index():
    s = request.args.get('s', '')
    data = get_all_posts(posts_file)
    return render_template('index.html', data=data, s=s)














