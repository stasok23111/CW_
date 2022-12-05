import json, pytest

posts_file = 'data/posts.json'
comment_file = 'data/comments.json'


def get_all_posts(filename):
    """
    загружает данные из json файла
    :param filename: путь к файлу
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_posts_by_user(user_name):
    """
    находит все посты пользователя
    :param user_name: имя пользователя
    """
    data = get_all_posts(posts_file)
    posts = []
    for i in data:
        if i['poster_name'].lower() == user_name.lower():
            posts.append(i)
    return posts



def get_comments_by_post_id(post_id):
    """
    ищет все комменты к данному посту
    :param post_id: номер поста
    """
    with open(comment_file, 'r', encoding='utf-8') as file:
        data_comment = json.load(file)
    data_posts = get_all_posts(posts_file)
    comment_posts = []
    for i in data_posts:
        if i['pk'] == post_id:
            for k in data_comment:
                 if k['post_id'] == post_id:
                    comment_posts.append(k)
    return comment_posts




def search_for_posts(query):
    """
    ищет посты содержащие определенное слово
    :param query: любое слово

    """
    data = get_all_posts(posts_file)
    posts = []
    for i in data:
        if query.lower() in i['content'].lower():
            posts.append(i)

    return posts


def get_post_by_pk(pk):
    """
    ищет пост по его номеру
    :param pk: номер поста
    """
    data = get_all_posts(posts_file)
    for i in data:
        if i['pk'] == pk:
            return i




