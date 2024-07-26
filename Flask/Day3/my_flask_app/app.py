from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from models import Post
from db import db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:oz-password@localhost/post'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# blueprint 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

from routes.posts_routes import post_blp

api = Api(app)
api.register_blueprint(post_blp)

from flask import render_template
@app.route('/manage-posts')
def manage_posts():
    return render_template('posts.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)