from flask import Flask
from flask import render_template
from flask_debug import Debug

app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def index():
    return '<div>Here</div>'

@app.route('/template')
@app.route('/template/<name>')
def template(name=None):
    return render_template('template.html', name=name)

@app.route('/raw')
def raw():
    return app.send_static_file("hello.htm")

Debug(app)
app.run(debug=True)