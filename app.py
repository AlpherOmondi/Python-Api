from flask import jsonify, Flask, request  # These are packages needed.import
# """
# Jsonify is here to convert lists to json. Language translator
# """
from http import HTTPStatus  # This enum includes different codes.

# Instance of flask
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


@app.route('/recipes', methods=['GET'])  # If we dont specify the default will be get
def get_recipes():
    return jsonify(recipes)


# Get a specific item
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
# The syntax means the value will be assigned to an integer variable.
# The function will then loop through recipes to locate the recipe that has is.
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
    return jsonify(recipe)
# Create recipe route
@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()  # This used to get the name and description
    name = data.get('name')
    description = data.get('description')
    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description

    }
    if recipes.append(recipe):
        return jsonify(recipe), HTTPStatus.CREATED
    else:
        return jsonify({'message': 'Error when posting'})


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
    data = request.get_json()
    recipe.update(
        {
            'name': data.get('name'),
            'description': data.get('description')
        }
    )
    return jsonify(recipe)


if __name__ == '__main__':
    app.run(debug=True)
