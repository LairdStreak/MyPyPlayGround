from flask import Flask
from flask import render_template
from flask import json, request
from flask_debug import Debug

app = Flask(__name__)

print(__name__)

@app.route('/')
def default_route():
    return render_template('default.html')

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

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)    

# Debug(app)
app.run(port=1000, debug=True)