# Python Standard Library Dependencies
import os

# External Dependency Imports
from datetime import timedelta
from dotenv import load_dotenv
from urllib import parse

# Internal Dependency Imports


##########################################################################################
#                                        Notes:                                          #
#                                                                                        #
# Things done in this file:                                                              #
# 1. Load the environment variables from the .env file                                   #
# 2. Define the configuration for the flask app with production and development defaults #
#                                                                                        #
##########################################################################################

# Load the environment variables from the .env file
load_dotenv()

# Define the configurations for the development and production environments and define function for setup
class ProdConfig:
    SECRET_KEY = os.environ["SECRET_KEY"]
    DEBUG = False
    ASSET_DEBUG = False
    SERVER_NAME = os.environ["SERVER_NAME"]
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    MONGO_URI = os.environ["DB_URI"].replace("[password]", parse.quote_plus(os.environ["DB_PASSWORD"]))

class DevConfig(ProdConfig):
    DEBUG = True
    ASSET_DEBUG = True
    SERVER_NAME = None

def configure(app):
    if os.environ.get("FLASK_ENV") == "production":
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(DevConfig)