from flask import jsonify, Flask, request # These are packages needed.import
# """
# Jsonify is here to convert lists to json. Language translator
# """
from http import HTTPStatus # This enum includes different codes.

#Instance of flask
app = Flask(__name__)
# Data
recipes = [
    {
        'id': 1,
        'name': 'Egg salad',
        'description': 'This is a lovely egg salad recipe'

    },
    {
        'id': 2,
        'name': 'Tomato Pasta',
        'description': 'This is a lovely tomato recipe'
    }

]
@app.route('/recipes',methods=['GET']) # If we dont specify the default will be get
def get_recipes():
    return jsonify(recipes)
# Get a specific item
