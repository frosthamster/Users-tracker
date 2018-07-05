from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment

db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
moment = Moment()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    from app.errors import bp as err_bp
    app.register_blueprint(err_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app


from app import models
