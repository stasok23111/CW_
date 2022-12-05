import logging

from flask import render_template, Blueprint, jsonify
from utils.utils import get_all_posts, get_post_by_pk

posts_file = "data/posts.json"

api_blueprint = Blueprint('api_blueprint', __name__)

logging.basicConfig(filename="api.log", level=logging.INFO)



@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts_():
    return jsonify(get_all_posts(posts_file))


@api_blueprint.route('/api/posts/<int:id>', methods=['GET'])
def get_posts_by_id(id):
    return jsonify(get_post_by_pk(id))
