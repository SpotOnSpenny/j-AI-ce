# Python Standard Library Dependencies


# External Dependency Imports


# Internal Dependency Imports


#######################################################################################
#                                        Notes:                                       #
#                                                                                     #
# This file defines the models for the database, and exports a list of collections to #
# create and/or drop based on the models defined. We also define a jsonSchema         #
# validator for each collection here so that we can validate any data that is created #
#                                                                                     #
#######################################################################################

example_model = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["field_x"],
        "properties": {
            "field_x": {
                "bsonType": "string",
                "description": "must be a string and IS required"
            },
            "field_y": {
                "bsonType": ["null", "string"],
                "description": "must be a string and is NOT required"
            }
        }
    }
}

models_and_schemas = {
    "collection1": example_model
}
# Test code below
if __name__ == '__main__':
    pass # Replace this with function calls or test code