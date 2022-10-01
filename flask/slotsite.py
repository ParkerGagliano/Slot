from re import L
from flask import Flask
from flask import Flask, render_template, url_for, flash, redirect
import jyserver.Flask as jsf
import numpy as np
import random as rand
app = Flask(__name__)


@jsf.use(app)
class App:
    def __init__(self):
        self.odds = 10
        self.money = 10000
        self.wager = 10
        self.canSpin = True
        self.lastWin = 0
        self.board = self.createBoard()

    def renderBoard(self):
        for i in range(3):
            for x in range(5):
                self.js.document.getElementById(
                    f'{i}{x}').innerHTML = self.board[i][x]

    def renderElse(self):
        self.js.document.getElementById(
            'balance').innerHTML = f'Current Balance: ${self.money}'
        self.js.document.getElementById(
            'currentbet').innerHTML = f'Current Bet: ${self.wager}'
        self.js.document.getElementById(
            'volatility').innerHTML = self.odds

    def createBoard(self):
        if self.canSpin:
            board = []
            temp = []
            for _ in range(3):
                for _ in range(5):
                    temp.append(rand.randint(0, self.odds))
                board.append(temp)
                temp = []
            return board

    def spin(self):
        self.js.document.getElementById('win').innerHTML = ""
        self.board = self.createBoard()
        self.bet()
        self.renderBoard()
        self.renderElse()

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
        if int(self.wager) > self.money:
            self.redBorder('balance', True)
            self.canSpin = False
        else:
            self.redBorder('balance', False)
            self.canSpin = True

            self.money = self.money - int(self.wager)
            multi = int(self.checkBoard())
            if self.odds == 3:
                multi = multi * 2
            if self.odds == 5:
                multi = multi * 5
            if self.odds == 10:
                multi = multi * 9
            final = int(self.wager) * (multi*2)
            self.lastWin = final
            if multi >= 1:
                self.js.document.getElementById(
                    'win').innerHTML = f'You won ${self.lastWin}!'
            else:
                self.js.document.getElementById(
                    'win').innerHTML = ""
            self.money = self.money + final

    def changeWager(self, ud):
        if ud == 1:
            self.wager += 10
            self.redBorder('currentbet', False)
        else:
            if self.wager <= 10:
                self.redBorder('currentbet', True)
            else:
                self.wager -= 10
        self.renderElse()

    def redBorder(self, name, on):
        if on:
            self.js.document.getElementById(name).style.color = "red"
        else:
            self.js.document.getElementById(name).style.color = "black"

    def changeVolatility(self, value):
        self.odds = value
        self.renderElse()


@ app.route('/')
def hello():
    return App.render(render_template('home.html'))


if __name__ == '__main__':
    app.run(debug=1)
