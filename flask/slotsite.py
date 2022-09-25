from flask import Flask
from flask import Flask, render_template, url_for, flash, redirect
from Test import Game
app = Flask(__name__)




@app.route('/')
def hello():
    test = Game(100)
    return render_template('home.html',test = test)


if __name__ == '__main__':
    app.run(debug=1)