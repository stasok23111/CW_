from flask import Flask, request, render_template
from app.main.views import main_blueprint
from app.detailed_post.views import detailed_post_blueprint
from app.search.views import search_blueprint
from app.user_feed.views import user_feed_blueprint
from api.api_blueprint import api_blueprint







app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)
app.register_blueprint(detailed_post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run()
