import pytest

from utils.utils import get_all_posts, get_post_by_pk
posts_file = "../data/posts.json"

def test_all_posts():
    assert type(get_all_posts(posts_file)) == list

expected_keys = ['poster_name', 'poster_avatar', 'pic', 'content',
                 'views_count', 'likes_count', 'pk']

def test_keys_in_get_all_posts():
    for post in get_all_posts(posts_file):
        kyes = [key for key in post.keys()]
        assert kyes == expected_keys


def test_get_post_by_pk():
    for i in range(1, 8):
        assert type(get_post_by_pk(i)) == dict      # при выполнении этого теста в utils
                                                    # нужно менять posts_file пока не нашёл как
                                                    # это исправить (../data/posts.json)



def test_keys_in_get_post_by_pk():
    for i in range(1, 8):                                # при выполнении этого теста в utils
        kyes = [key for key in get_post_by_pk(i).keys()] # нужно менять posts_file пока не нашёл как
        assert kyes == expected_keys                     # это исправить (../data/posts.json)










