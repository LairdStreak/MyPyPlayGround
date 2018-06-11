from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('default.html')


@app.route('/index')
def index():
    return app.send_static_file("hello.htm")


def main():
    app.run()


if __name__ == '__main__':
    main()
