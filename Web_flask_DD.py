from flask import Flask
from flask import request
from flask import redirect

app = Flask(__name__)
'''
@app.route('/')
def index():
    return r'<h1>Hello World Python</h1>'
'''

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return r'<p>Your browser is : {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {} !</h1>'.format(name)


@app.route('/site')
def redir():
    return redirect('https://www.python.org/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)