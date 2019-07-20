from flask import Flask, Markup
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
from flaskext.markdown import Markdown
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
pagedown = PageDown(app)
Markdown(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models