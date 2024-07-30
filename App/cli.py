# Python Standard Library Dependencies


# External Dependency Imports


# Internal Dependency Imports
from App.Data.db_models import models_and_schemas

#######################################################################################
#                                        Notes:                                       #
#######################################################################################

# Define the utility functions for the CLI commands
def drop_collections(app):
    collections = app.mongo.db.list_collection_names()
    if collections != []:
        for collection in collections:
            app.mongo.db[collection].drop()
            app.logger.info(f"Collection {collection} dropped via CLI")
        print("All collections dropped")
    else:
        print("No tables to drop")

def create_collections(app):
    collections = app.mongo.db.list_collection_names()
    for model in models_and_schemas:
        if model not in collections:
            app.mongo.db.create_collection(model, validator=models_and_schemas[model])
            app.logger.info(f"Collection {model} created via CLI")
            print(f"Collection {model} created")
        else:
            print(f"Collection {model} already exists")

# Register the actual CLI commands for use
def register_cli(app):
    @app.shell_context_processor
    def make_shell_context():
        return {"app": app}
    
    @app.cli.command("init", help="Drops all tables in the database and recreates them")
    def init():
        drop_collections(app)
        create_collections(app)


# Test code below
if __name__ == '__main__':
    pass # Replace this with function calls or test code