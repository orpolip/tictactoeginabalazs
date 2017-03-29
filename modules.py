
# def decor(func):
# def wrap():
# print("************************************")
# func()
# print("************************************")
# return wrap


def print_text():
    print("************************************")
    print(" Welcome to TicTacToe!")
    print("************************************")

# def decor(func):
    # def wrap():
    # func()
    # print("-------------------------------------------------------------------------------------------------")
    # return wrap


def print_text2():
    print("INSTRUCTIONS: Use the numbers between 1-9, to place your mark. Press r to restart, or q to quit.")
    print("-------------------------------------------------------------------------------------------------")


def checkLine(char, board):  # paraméterrel hívni(boardosfasz)
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


def show(board):  # paraméterrel hívni(boardosfasz)
    print(board[7], '|', board[8], '|', board[9])
    print("---------")
    print(board[4], '|', board[5], '|', board[6])
    print("---------")
    print(board[1], '|', board[2], '|', board[3])


def restartgame(step1, board, board1):  # paraméterrel hívni(boardosfasz)
    decorated = decor(print_text2)
    decorated()
    show(board1)
    return board == [" "] * 10
    return step1 == 0


def comprandom(signal, step1, board):  # paraméterrel hívni(boardosfasz)
    import random
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
            if checkLine('X', board):
                board[i] = " "
                return i
            else:
                board[i] = " "

        for i in emptylist:

            board[i] = "O"
            if checkLine('O', board):
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
            if checkLine('O', board):
                board[i] = " "
                return i
            else:
                board[i] = " "

        for i in emptylist:

            board[i] = "X"
            if checkLine('X', board):
                board[i] = " "
                return i
            else:
                board[i] = " "

        return random.choice(emptylist)
