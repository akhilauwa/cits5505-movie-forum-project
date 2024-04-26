import os
from dotenv import load_dotenv

# Get the base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

# Load environment variables from .env file
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'the_super_secret_key_to_cits5505_movie_forum_project' # Secret key for CSRF protection
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app', 'app.db') # Database location
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Turn off update messages from SQLAlchemy
