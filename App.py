# ---- Flask Hello World ---- #
# Import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# Use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/hello")

# Define the view using a function, which returns a string
def hello_world():
    return "Hello, Sandeep!"

# Start the development server using the run() method

if __name__ == "__main__":
    app.run()