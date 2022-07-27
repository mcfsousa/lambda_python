import json

def get_schema(schema_name):
    with open(schema_name, 'r') as file:
        schema = json.load(file)
        return schema
