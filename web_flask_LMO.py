from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}<p>'.format(user_agent)
    #return '<h1>Hello world !</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {} !</h1>'.format(name)

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
