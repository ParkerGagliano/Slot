from flask import Flask
from flask import Flask, render_template, url_for, flash, redirect
from Test import Game
import jyserver.Flask as jsf
import numpy as np
import random as rand
app = Flask(__name__)


@jsf.use(app)
class App:
    def __init__(self):
        self.board = self.createBoard()
        self.money = 10000  # Set self variable count equal to 0

    def renderBoard(self):
        self.js.document.getElementById(
            'balance').innerHTML = f'Current Balance: {self.money}'
        for i in range(3):
            for x in range(5):
                self.js.document.getElementById(
                    f'{i}{x}').innerHTML = self.board[i][x]

    def createBoard(self):
        board = []
        temp = []
        for _ in range(3):
            for _ in range(5):
                temp.append(rand.randint(0, 10))
            board.append(temp)
            temp = []
        return board

    def spin(self):
        self.js.document.getElementById('win').innerHTML = ""
        self.board = self.createBoard()
        self.bet()
        self.renderBoard()

    def checkBoard(self):
        matches = 0
        temp = np.array(self.board)
        for i in range(temp.shape[0]):
            if np.all(temp[i] == temp[i][0]):
                matches += 1
        trans_arr = temp.T
        for i in range(trans_arr.shape[0]):
            if np.all(trans_arr[i] == trans_arr[i][0]):
                matches += 1
        return matches

    def bet(self):
        joe = self.js.document.getElementById('bet')
        bet = joe.value
        if int(bet) > self.money:
            print('You cant bet more then you have')
        else:
            self.money = self.money - int(bet)
            multi = int(self.checkBoard())
            if multi >= 1:
                self.js.document.getElementById('win').innerHTML = "You won!"
            final = int(bet) * (multi*2)
            self.money = self.money + final


@app.route('/')
def hello():
    return App.render(render_template('home.html'))


if __name__ == '__main__':
    app.run(debug=1)
