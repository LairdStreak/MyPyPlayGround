from flask import Flask
from flask import render_template
from flask_debug import Debug
from tvmazereader import main

app = Flask(__name__)

@app.route('/')
def default_route():
    getData()
    return render_template('tvMazeData.html')

def getData():
    main()


Debug(app)
app.run(port=1100)
