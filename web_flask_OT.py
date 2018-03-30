from flask import Flask
from flask import request
from flask import redirect, render_template


app = Flask(__name__)

#decorator
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1>\n<p> Your Browser is {}</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/site')
def redir():
    return redirect('https://www.python.org/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)



########################################################################################################################
