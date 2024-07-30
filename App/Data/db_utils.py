# Python Standard Library Dependencies


# External Dependency Imports
from flask import current_app

# Internal Dependency Imports

#######################################################################################
#                                        Notes:                                       #
#                                                                                     #
# This file defines the creation, reading, and updating of documents within the Mongo #
# database.
#######################################################################################


def add_document(app, field_x, field_y=None):
    """
    Inserts a document into _______ collection with the following fields:
        collection (str): The name of the collection to add the document to.
        field_x (str): The name of the first field in the document.
        field_y (str): The name of the second field in the document.
    """
    doccument = {
        "field_x": field_x,
        "field_y": field_y
    }
    with app.app_context():
        app.mongo.db.collection1.insert_one(doccument)
        print("Document added to collection_1")