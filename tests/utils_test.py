import pytest
import json

from utils.utils import get_all_posts, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk

posts_file = 'data/posts.json'

with open(posts_file, 'r', encoding='utf-8') as file:
    data = json.load(file)


def test_get_all_posts():
    assert get_all_posts(posts_file) == data

def test_get_posts_by_user():
    for i in data:
        assert len(get_posts_by_user(i['poster_name'])) == 2

def test_get_comments_by_post_id():
    assert len(get_comments_by_post_id(1)) == 4
    assert len(get_comments_by_post_id(2)) == 4
    assert len(get_comments_by_post_id(3)) == 4
    assert len(get_comments_by_post_id(4)) == 4
    assert len(get_comments_by_post_id(5)) == 2
    assert len(get_comments_by_post_id(6)) == 1
    assert len(get_comments_by_post_id(7)) == 1
    assert len(get_comments_by_post_id(8)) == 0


def test_search_for_posts():
    assert len(search_for_posts('пирог')) == 1

def test_get_post_by_pk():
    for i in range(len(data)):
        assert get_post_by_pk(i + 1) == data[i]



