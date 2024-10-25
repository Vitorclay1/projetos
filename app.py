from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """
    This function is a simple Flask route that returns a welcome message.

    Parameters:
    None

    Returns:
    str: A string containing the welcome message 'Hello, World!'
    """
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'pagina sobre'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)