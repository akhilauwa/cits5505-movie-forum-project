from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create an instance of the SQLAlchemy class
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

def create_app(config_class=Config):
    # Create a Flask application
    app = Flask(__name__, title='CITS5505 Movie Forum')
    # Load the configuration from the config.py file
    app.config.from_object(config_class)
    # Initialize the database
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Import the routes module
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app