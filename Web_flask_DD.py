from flask import Flask
from flask import request
from flask import redirect, render_template

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


@app.route('/test/<name>')
def test(name):
    return '<h1>Hello {} !</h1>'.format(name)

@app.errorhandler(404)
def page_not_found(err):
    return render_template('tpl_DD.html'), 404

@app.route('/site')
def site(name):
    return render_template('index__DD.html', name=name)

@app.route('/site')
def redir():
    return redirect('https://wwww.infodims.com')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)