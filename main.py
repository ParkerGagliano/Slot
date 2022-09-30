
from Game import Game


def main():
    isPlaying = False
    while isPlaying == False:
        money = int(
            input('Welcome, how much money would you like to start with?'))
        if isinstance(money, int) and money > 0:
            isPlaying = True
            game = Game(money)
            while True:
                wager = input('How much would you like to bet?')
                print(game.board)
                game.bet(wager)
                print(f'Balance: ${game.money}')
                if game.money <= 0:
                    print('You lost all your money!')
                    break
        else:
            print('Please enter a valid amoun0t of money')


def odds():
    tracker = {}
    for i in range(100000):
        game = Game(10000000)
        matches = game.checkBoard()
        game.spin()
        if matches in tracker:
            tracker[matches] += 1
        else:
            tracker[matches] = 1

    for i in tracker:
        print(i, tracker[i])


if __name__ == '__main__':
    main()
