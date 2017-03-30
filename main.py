import sys
import pyglet
from modules import *
from seppukumode import *
from anim_title import *
import os

play_sound(play_sound)
pass
sep = sep(sep)
difficulty = difficulty(difficulty)
print_text3()
mode = mode(mode)
gameisplaying = 1

if mode == "1":
    Player1 = input("Player1, enter your name here (max 20 characters): ")
    while len(Player1) > 20:
        while len(Player1) > 35:
            print("Dude, I feel like You're bugtesting here (or You have a damn long name)... try again")
            Player1 = input(":")
            continue
        else:
            pass

        while 35 > len(Player1) > 20:
            print("Please try to define yourself in max. 20 characters. Try again.")
            Player1 = input(":")
            continue
        else:
            pass
    else:
        pass

    Player2 = input("Player2, enter your name here (max 20 characters): ")
    while len(Player2) > 20:
        while len(Player2) > 35:
            print("Dude, I feel like You're bugtesting here (or You have a damn long name)... try again")
            Player2 = input(":")
            continue
        else:
            pass

        while 35 > len(Player2) > 20:
            print("Please try to define yourself in max. 20 characters. Try again.")
            Player2 = input(":")
            continue
        else:
            pass
    else:
        pass

if mode == "2":
    Player1 = input("Enter your name here (max 20 characters): ")
    while len(Player1) > 20:
        while len(Player1) > 35:
            print("Dude, I feel like You're bugtesting here (or You have a damn long name)... try again")
            Player1 = input(":")
            continue
        else:
            pass

        while 35 > len(Player1) > 20:
            print("Please try to define yourself in max. 20 characters. Try again.")
            Player1 = input(":")
            continue
        else:
            pass
    else:
        pass


if mode == "3":
    Player2 = input("Enter your name here (max 20 characters): ")
    while len(Player2) > 20:
        while len(Player2) > 35:
            print("Dude, I feel like You're bugtesting here (or You have a damn long name)... try again")
            Player2 = input(":")
            continue
        else:
            pass

        while 35 > len(Player2) > 20:
            print("Please try to define yourself in max. 20 characters. Try again.")
            Player2 = input(":")
            continue
        else:
            pass
    else:
        pass
board1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
wins_p1 = 0
wins_p2 = 0


show(board1)


board = [" "] * 10


attack1 = "a"
attack2 = "a"
step1 = 0
dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

while gameisplaying:
    while True:
        if attack1 == "r" or attack2 == "r":
            sep = input("Select game style: Traditional (1) Seppuku(2): ")
            if sep == "q":
                print("GOOD BYE!")
                sys.exit(0)
            while sep != "1" and sep != "2":
                print("Game style have to be set 1 or 2")
                sep = input(":")
                continue
            else:
                sep = int(sep)
                pass
            difficulty = input("Select difficulty level: Amateur (1) Godlike(2): ")
            if difficulty == "q":
                print("GOOD BYE!")
                sys.exit(0)
            while difficulty != "1" and difficulty != "2":
                print("Difficulty have to set 1 or 2")
                difficulty = input(":")
                continue
            else:
                difficulty = int(difficulty)
                pass
            mode = input("Please select a game mode: (1) Human vs Human, (2) Human vs Computer, (3) Computer vs Human: ")
            if mode == "q":
                print("GOOD BYE!")
                sys.exit(0)
            while mode != "1" and mode != "2" and mode != "3":
                print("mode must be 1,2, or 3")
                mode = input(": ")
                continue
            else:
                pass
            if mode == "1" or mode == "2":
                step1 = 0
                Player1 = input("Player1, enter your name here (max 20 characters): ")
                while len(Player1) > 20:
                    while len(Player1) > 35:
                        print("Dude, I feel like You're bugtesting here (or You have a damn long name)... try again")
                        Player1 = input(":")
                        continue
                    else:
                        pass

                    while 35 > len(Player1) > 20:
                        print("Please try to define yourself in max. 20 characters. Try again.")
                        Player1 = input(":")
                        continue
                    else:
                        pass
                else:
                    pass
            if mode == "1" or mode == "3":
                step1 = 0
                Player2 = input("Player2, enter your name here (max 20 characters): ")
                while len(Player2) > 20:
                    while len(Player2) > 35:
                        print("Dude, I feel like You're bugtesting here (or You have a damn long name)... try again")
                        Player2 = input(":")
                        continue
                    else:
                        pass

                    while 35 > len(Player2) > 20:
                        print("Please try to define yourself in max. 20 characters. Try again.")
                        Player2 = input(":")
                        continue
                    else:
                        pass
                else:
                    pass
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
                dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
                continue
            if attack1 == "q":
                print("GOOD BYE!")
                sys.exit(0)
            attack1 = int(attack1)

            if board[attack1] != 'X' and board[attack1] != 'O':
                board[attack1] = 'X'
                dic[attack1] = 1
                step1 = step1 + 1
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

    if sep == 2:
        seppuku("O", board, dic)
    show(board)

    if checkLine('X', board):
        play_winsound(play_winsound)
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
            print("GOOD BYE!")
            os._exit(0)
        if user_input == "y":
            restartgame(step1, board, board1)
            dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            continue
    if step1 == 5 and checkLine('X', board) != True and sep == 1:
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
            print("GOOD BYE!")
            os._exit(0)
        if user_input == "y":
            restartgame(step1, board, board1)
            dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
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
                print("-" + Player2 + " restarted the game-")
                board = [" "] * 10
                step1 = 0
                restartgame(step1, board, board1)
                dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
                break
            if attack2 == "q":
                print("GOOD BYE!")
                sys.exit(0)
            attack2 = int(attack2)
            if board[attack2] != 'O' and board[attack2] != 'X':
                board[attack2] = 'O'
                dic[attack2] = 2
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
        if sep == 2:
            seppuku("X", board, dic)
        show(board)

    if checkLine('O', board):
        play_winsound(play_winsound)
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
            print("GOOD BYE!")
            os._exit(0)
        if user_input == "y":
            restartgame(step1, board, board1)
            dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            continue
        continue
