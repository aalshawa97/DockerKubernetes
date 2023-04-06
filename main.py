#Abdullah Mutaz Alshawa
#4/6/23
# Import the Flask and request modules
from flask import Flask, request

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL path
@app.route('/')
def welcome():
    # Return a 'Welcome' message to the client
    return 'Welcome to the DevOps Demo'

# Define a route for the '/goodbye' URL path
@app.route('/goodbye')
def goodbye():
    # Get the value of the 'name' query parameter from the request URL
    name = request.args.get('name')
    # Return a 'Goodbye, [name]!' message to the client using an f-string
    return f'Goodbye, {name}!'

# If this script is being run as the main program
if __name__ == '__main__':
    # Start the Flask application with debug mode enabled and listen on all network interfaces
    app.run(debug=True, host='0.0.0.0')
