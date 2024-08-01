# Python Standard Library Dependencies
import os
import logging

# External Dependency Imports
from flask import Flask, current_app, Blueprint
from flask_assets import Environment, Bundle
from flask_pymongo import PyMongo

# Internal Dependency Imports
from App.config import configure
from App.cli import register_cli
from App.Data.db_models import models_and_schemas

#######################################################################################
#                                        Notes:                                       #
#                                                                                     #
# Things done in this file:                                                           #
# 1. Set up logging for the application
# 2. Initiate the flaskapp                                                            #
# 3. Package the assets for the site                                                  #
# 4. Register the CLI commands for the flask app                                      #
# 5. Import blueprints for the aapp                                                   #
# 6. Instantiate mongo as db and connect to it                                        #
#                                                                                     #
#######################################################################################

def create_app():
    # Set up logging for the application
    if not os.path.exists("logs"):
        os.mkdir("logs")
    logging.basicConfig(filename="logs/record.log", level=os.environ["LOG_LEVEL"],
                        format="%(asctime)s %(levelname)s: %(message)s")

    # Initiate the flaskapp
    app = Flask(__name__, static_folder="static", template_folder="templates")
    configure(app)

    # Package the assets for the site
    assets = Environment(app)

    assets.register(
        "css_all",
        Bundle(
            "css/bootstrap.min.css",
            "css/all_css.css",
            output="min_assets/all.css",
            filters="cssmin"
        )
    )

    assets.register(
        "js_all",
        Bundle(
            "js/*.js",
            output="min_assets/all.js",
            filters="jsmin"
        )
    )

    # Register the CLI commands for the flask app
    register_cli(app)

    # Create and import blueprints here
    from App.Main.main import main_blueprint
    app.register_blueprint(main_blueprint)

    # Instantiate mongo as db, connect to it, and ensure necessary collections exist, we also add schemas here
    app.mongo = PyMongo(app)
    existing = app.mongo.db.list_collection_names()
    needed = models_and_schemas.keys()
    for collection in needed:
        if collection not in existing:
            app.mongo.db.create_collection(collection, validator=models_and_schemas[collection])
            app.logger.info(f"Collection {collection} created as it did not exist")

    return app

