from flask import Flask
from flask import Flask, render_template, url_for, flash, redirect
from Test import Game
app = Flask(__name__)
test = Game(100)
nums = test.createBoard()

@app.route('/')
def hello():
    return render_template('home.html', nums = nums)


if __name__ == '__main__':
    app.run(debug=1)