from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return r'<h1>Hello World Python</h1>'

## 
if __name__ == '__main__':
    app.run(debug=True)