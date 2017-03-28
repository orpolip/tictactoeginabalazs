import sys
import random
print("Modes: Human vs. Human (1) - Human vs. Computer (2) - Computer vs. Human (3)")

mode = input("Please select a game mode: ")
while mode != "1" and mode != "2" and mode != "3":
    print("mode must be 1,2, or 3")
    mode = input(": ")

gameisplaying = 1

if mode == "1":
    Player1 = input("Player1, enter your name here: ")
    Player2 = input("Player2, enter your name here: ")
if mode == "2":
    Player1 = input("Enter your name here: ")
if mode == "3":
    Player2 = input("Enter your name here: ")

wins_p1 = 0
wins_p2 = 0

board1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def show1():
    print(board1[7], '|', board1[8], '|', board1[9])
    print("---------")
    print(board1[4], '|', board1[5], '|', board1[6])
    print("---------")
    print(board1[1], '|', board1[2], '|', board1[3])


def decor(func):
    def wrap():
        print("************************************")
        func()
        print("************************************")
    return wrap


def print_text():
    print(" Welcome to TicTacToe!")


decorated = decor(print_text)
decorated()


def decor(func):
    def wrap():
        func()
        print("-------------------------------------------------------------------------------------------------")
    return wrap


def print_text2():
    print("INSTRUCTIONS: Use the numbers between 1-9, to place your mark. Press r to restart, or q to quit.")


decorated = decor(print_text2)
decorated()

show1()


def checkLine(char):
    if board[1] == char and board[2] == char and board[3] == char:
        return True
    if board[4] == char and board[5] == char and board[6] == char:
        return True
    if board[7] == char and board[8] == char and board[9] == char:
        return True
    if board[1] == char and board[5] == char and board[9] == char:
        return True
    if board[3] == char and board[5] == char and board[7] == char:
        return True
    if board[1] == char and board[4] == char and board[7] == char:
        return True
    if board[2] == char and board[5] == char and board[8] == char:
        return True
    if board[3] == char and board[6] == char and board[9] == char:
        return True


board = [" "] * 10


def show():
    print(board[7], '|', board[8], '|', board[9])
    print("---------")
    print(board[4], '|', board[5], '|', board[6])
    print("---------")
    print(board[1], '|', board[2], '|', board[3])


attack1 = "a"
attack2 = "a"
step1 = 0


def restartgame():
    decorated = decor(print_text2)
    decorated()
    show1()
    return board == [" "] * 10
    return step1 == 0


def comprandom(signal):
    if signal == "X" and step1 == 0:
        slots = (1, 3, 5, 7, 9)
        return random.choice(slots)

    if signal == "X" and step1 == 1:
        if (board[1] == "X" or board[9] == "X") and (board[7] == " "):
            return 7
        if (board[1] == "X" or board[9] == "X") and (board[3] == " "):
            return 3
        if (board[3] == "X" or board[7] == "X") and (board[1] == " "):
            return 1
        if (board[3] == "X" or board[7] == "X") and (board[9] == " "):
            return 9
        if board[5] == "X":
            blist = []
            for i in range(1, 10, 2):
                if board[i] == " ":
                    blist.append(i)
            return random.choice(blist)

    if signal == "X" and step1 > 1:
        emptylist = []
        for i in range(1, 10):
            if board[i] == " ":
                emptylist.append(i)

        for i in emptylist:

            board[i] = "X"
            if checkLine('X'):
                board[i] = " "
                return i
            else:
                board[i] = " "

        for i in emptylist:

            board[i] = "O"
            if checkLine('O'):
                board[i] = " "
                return i
            else:
                board[i] = " "

        return random.choice(emptylist)

    if signal == "O" and step1 == 1:
        for i in range(1, 10):
            if board[i] == "X":
                memi = i
        slots = []
        for i in range(1, 10, 2):
            if i != memi:
                slots.append(i)
        return random.choice(slots)

    if signal == "O" and step1 > 1:
        emptylist = []
        for i in range(1, 10):
            if board[i] == " ":
                emptylist.append(i)

        for i in emptylist:

            board[i] = "O"
            if checkLine('O'):
                board[i] = " "
                return i
            else:
                board[i] = " "

        for i in emptylist:

            board[i] = "X"
            if checkLine('X'):
                board[i] = " "
                return i
            else:
                board[i] = " "

        return random.choice(emptylist)


while gameisplaying:
    while True:
        if attack1 == "r" or attack2 == "r":
            mode = input("Please select a game mode: ")
            while mode != "1" and mode != "2" and mode != "3":
                print("mode must be 1,2, or 3")
                mode = input(": ")
            if mode == "1" or mode == "2":
                step1 = 0
                Player1 = input("Player1, enter your name here: ")
            if mode == "1" or mode == "3":
                step1 = 0
                Player2 = input("Player2, enter your name here: ")
            wins_p1 = 0
            wins_p2 = 0

        try:
            if mode == "1" or mode == "2":
                attack1 = input(Player1 + " select a spot: ")
            else:
                print("Computer moved")
                attack1 = comprandom("X")
            if attack1 == "r":
                print("-" + Player1 + " restarted the game-")
                board = [" "] * 10
                step1 = 0
                restartgame()
                continue
            if attack1 == "q":
                sys.exit(0)
            attack1 = int(attack1)

            if board[attack1] != 'X' and board[attack1] != 'O':
                board[attack1] = 'X'
                step1 = step1 + 1
                break
            else:
                print("This spot is taken.")
                continue

        except IndexError:
            print("As i said before you have to choose a number between 1 and 9. Try again!")
            continue
        except ValueError:
            print("As i said before you have to choose a !NUMBER! between 1 and 9. Try again!")
            continue

    show()

    if checkLine('X'):
        board = [" "] * 10
        step1 = 0
        wins_p1 += 1
        if mode == "1":
            print(Player1 + " won the game!")
            print(Player1 + ": " + str(wins_p1))
            print(Player2 + ": " + str(wins_p2))
            print("Do you want a rematch? (press y/n)")
        if mode == "2":
            print(Player1 + " won the game!")
            print(Player1 + ": " + str(wins_p1))
            print("Computer" + ": " + str(wins_p2))
            print("Do you want a rematch? (press y/n)")
        if mode == "3":
            print("Computer won the game!")
            print("Computer" + ": " + str(wins_p1))
            print(Player2 + ": " + str(wins_p2))
            print("Do you want a rematch? (press y/n)")
        user_input = input(":")

        while user_input != "y" and user_input != "n":
            print("y is for YES, n is for NO, it is not that hard...choose one")
            print("Do you want a rematch? y/n")
            user_input = input(": ")
        if user_input == "n":
            break
        if user_input == "y":
            restartgame()
            continue

    if step1 == 5 and checkLine('X') != True:
        board = [" "] * 10
        step1 = 0
        print("This is a draw!")
        if mode == "1":
            print(Player1 + ": " + str(wins_p1))
            print(Player2 + ": " + str(wins_p2))
        if mode == "2":
            print(Player1 + ": " + str(wins_p1))
            print("Computer: " + str(wins_p2))
        if mode == "3":
            print("Computer: " + str(wins_p1))
            print(Player2 + ": " + str(wins_p2))
        print("Do you want a rematch? (press y/n)")
        user_input = input(":")
        while user_input != "y" and user_input != "n":
            print("y is for YES, n is for NO, it is not that hard...choose one")
            print("Do you want a rematch? y/n")
            user_input = input(": ")
        if user_input == "n":
            break
        if user_input == "y":
            restartgame()
            continue

    while True:

        try:
            if mode == "1" or mode == "3":
                attack2 = input(Player2 + " it's your turn now:")
            else:
                print("computer moved")
                attack2 = comprandom("O")
            if attack2 == "r":
                print("-Player 2 restarted the game-")
                board = [" "] * 10
                step1 = 0
                restartgame()
                break
            if attack2 == "q":
                sys.exit(0)
            attack2 = int(attack2)
            if board[attack2] != 'O' and board[attack2] != 'X':
                board[attack2] = 'O'
                break
            else:
                print("This spot is taken.")
                continue

        except IndexError:
            print("As i said before you have to choose a number between 1 and 9. Try again!")
            pass
        except ValueError:
            print("As i said before you have to choose a !NUMBER! between 1 and 9. Try again!")
            continue
    if attack2 != 'r':
        show()
    if checkLine('O'):
        board = [" "] * 10
        step1 = 0
        wins_p2 += 1
        if mode == "1":
            print(Player2 + " won the game!")
            print(Player1 + ": " + str(wins_p1))
            print(Player2 + ": " + str(wins_p2))
            print("Do you want a rematch? (press y/n)")
        if mode == "2":
            print("Computer won the game!")
            print(Player1 + ": " + str(wins_p1))
            print("Computer" + ": " + str(wins_p2))
            print("Do you want a rematch? (press y/n)")
        if mode == "3":
            print(Player2 + " won the game!")
            print("Computer" + ": " + str(wins_p1))
            print(Player2 + ": " + str(wins_p2))
            print("Do you want a rematch? (press y/n)")
        user_input = input(":")
        while user_input != "y" and user_input != "n":
            print("y is for YES, n is for NO, it is not that hard...choose one")
            print("Do you want a rematch? y/n")
            user_input = input(": ")
        if user_input == "n":
            break
        if user_input == "y":
            restartgame()
            continue
