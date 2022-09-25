import numpy as np
import random as rand

class Game():
    def __init__(self, money):
        self.board = self.createBoard()
        self.money = int(money)


    def createBoard(self):
        board=[]
        temp = []
        for _ in range(3):
            for _ in range(5):
                temp.append(rand.randint(0,2))
            board.append(temp)
            temp = []
        return(np.array(board))


    def spin(self):
        self.board = self.createBoard()

    def checkBoard(self):
        matches = 0
        for i in range(self.board.shape[0]):
            if np.all(self.board[i]==self.board[i][0]):
                matches+=1
        trans_arr = self.board.T
        for i in range(trans_arr.shape[0]):
            if np.all(trans_arr[i] == trans_arr[i][0]):
                matches+=1
        return matches

    def bet(self, bet):
        self.money = self.money - int(bet)
        multi = int(self.checkBoard())
        if multi >= 1:
            print("You won!")
        final = int(bet) * (multi*2)

        self.money = self.money + final
        self.spin()

        



        


