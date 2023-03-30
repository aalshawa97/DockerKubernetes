#Abdullah Mutaz Alshawa
#Docker tutorial

#Flask is a web development framework
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/goodbye')
def goodbye():
    name = request.args.get('name')
    return f'Goodbye, {name}!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
