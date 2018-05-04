from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Taniel"
    name = "Alanna"
    return render_template('index.html', author=author, name=name)


if __name__ == '__main__':
    app.run()