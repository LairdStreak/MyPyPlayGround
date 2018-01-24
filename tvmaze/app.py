from flask import Flask
from flask import render_template
from tvmazereader import main

app = Flask(__name__)

@app.route('/')
def default_route():
    data = main()
    return render_template('tvMazeData.html',data=data)

def getData():
    main()

if __name__ == '__main__':
    app.run()
