from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = '3813cc4046ed3d4262f52a6a7645b16d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'INPUT_MAIL_USERNAME'
app.config['MAIL_PASSWORD'] = 'INPUT_MAIL_PASSWORD'
mail = Mail(app)

with app.app_context():
    db.create_all()

from .users.routes import users
from .posts.routes import posts
from .main.routes import main   

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
# NOTE: '.' in the importation code lines mean current directory.
#       therefore in our case 'flaskblog' since it's our package dir. 