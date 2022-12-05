from flask import render_template, Blueprint, request
from utils.utils import get_comments_by_post_id, get_all_posts

posts_file = 'data/posts.json'

detailed_post_blueprint = Blueprint(
    'detailed_post_blueprint',
    __name__,
    template_folder='templates')


@detailed_post_blueprint.route('/post/<int:id>')
def page_index(id):
    data = get_all_posts(posts_file)
    comments = get_comments_by_post_id(id)
    len_comments = len(comments)
    return render_template('post.html', data=data, id=id - 1, comments=comments, len_comments=len_comments)
