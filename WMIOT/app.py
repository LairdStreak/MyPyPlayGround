from flask import Flask
from flask import json, request, jsonify
from flask import render_template, send_file
from flask_debugtoolbar import DebugToolbarExtension
import os.path
import wmiotdata
import plotwmiotdata as plt


app = Flask(__name__)
print(__name__)

@app.route('/')
@app.route('/index')
def default_route():
    return render_template('default.html')

@app.route('/template')
@app.route('/template/<name>')
def template(name=None):
    return render_template('template.html', name=name)

@app.errorhandler(404)
def page_not_found(_error):
    """Returns the default error page if there's a page not found error"""
    return render_template('error.html'), 404

@app.route('/messages', methods = ['POST','GET'])
def api_message():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'text/plain':
            return "Text Message: " + request.data

        elif request.headers['Content-Type'] == 'application/json':
            return "JSON Message: " + json.dumps(request.json)
    else:
        return "her5e"

@app.route('/data/', methods = ['POST'])
def api_data():
    if request.headers['Content-Type'] == 'application/json':
        try:
            data = request.json
            print(data)
            python_obj = json.loads(data)
            print(type(python_obj))
            temperature = python_obj['temp']
            humidity = python_obj['humid']
            print(temperature)
            print(humidity)
            wmiotdata.put_latestdata(temperature, humidity)
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        except Exception as e:
            message = str(e)
            print(message)
    else:
       return json.dumps({'success': False}), 400, {'ContentType': 'application/json'}

@app.route('/getdata/', methods = ['GET'])
def get_data():
    data = wmiotdata.fetch_latestdata()
    return jsonify(data)


@app.route('/temperatureplot.png', methods = ['GET'])
def get_temperatureplot():
    data = wmiotdata.fetch_temperature_for_last_day()
    img = plt.plot_dataframe(data)
    return send_file(img, mimetype='image/png')

app.debug = True
app.config['SECRET_KEY'] = '338ee998-7b72-4a3b-8df6-48c076b171b5'
toolbar = DebugToolbarExtension(app)
# Debug(app)
app.run(host='0.0.0.0', port=1000)