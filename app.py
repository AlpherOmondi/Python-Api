from flask import Flask # Import flask package

app = Flask(__name__) # Create an instance of Flask(Object)


@app.route('/') # Specify route
def hello_world():  # put application's code here First Api function
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
