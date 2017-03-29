import sys
from modules import *


difficulty = difficulty(difficulty)

print("Modes: Human vs. Human (1) - Human vs. Computer (2) - Computer vs. Human (3)")
mode = mode(mode)
gameisplaying = 1

if mode == "1":
    Player1 = input("Player1, enter your name here: ")
    Player2 = input("Player2, enter your name here: ")
if mode == "2":
    Player1 = input("Enter your name here: ")
if mode == "3":
    Player2 = input("Enter your name here: ")
board1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
wins_p1 = 0
wins_p2 = 0


print_text()
print_text2()

show(board1)


board = [" "] * 10


attack1 = "a"
attack2 = "a"
step1 = 0


while gameisplaying:
    while True:
        if attack1 == "r" or attack2 == "r":
            difficulty = input("Select difficulty level: Amateur (1) Godlike(2): ")
            while difficulty != "1" and difficulty != "2":
                print("Difficulty have to set 1 or 2")
                difficulty = input(":")
                continue
            else:
                difficulty = int(difficulty)
                pass
            mode = input("Please select a game mode: ")
            while mode != "1" and mode != "2" and mode != "3":
                print("mode must be 1,2, or 3")
                mode = input(": ")
                continue
            else:
                pass
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
                if difficulty == 2:
                    attack1 = comprandom("X", step1, board)
                if difficulty == 1:
                    attack1 = compbasic("X", step1, board)
            if attack1 == "r":
                print("-" + Player1 + " restarted the game-")
                board = [" "] * 10
                step1 = 0
                restartgame(step1, board, board1)
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

    show(board)  # show to ply2

    if checkLine('X', board):
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
            restartgame(step1, board, board1)
            continue

    if step1 == 5 and checkLine('X', board) != True:
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
            restartgame(step1, board, board1)
            continue

    while True:

        try:
            if mode == "1" or mode == "3":
                attack2 = input(Player2 + " it's your turn now:")
            else:
                print("computer moved")
                if difficulty == 2:
                    attack2 = comprandom("O", step1, board)
                if difficulty == 1:
                    attack2 = compbasic("O", step1, board)
            if attack2 == "r":
                print("-Player 2 restarted the game-")
                board = [" "] * 10
                step1 = 0
                restartgame(step1, board, board1)
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
        show(board)  # show to ply1
    if checkLine('O', board):
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
            restartgame(step1, board, board1)
            continue
