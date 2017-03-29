def seppuku(char, board, dic):
    for k in dic:
        if char == "X":
            if dic[k] % 2 != 0:
                dic[k] = dic[k] + 2
        if char == "O":
            if dic[k] % 2 == 0 and dic[k] > 0:
                dic[k] = dic[k] + 2
    for k in dic:
        if char == "X":
            if dic[k] == 9:
                dic[k] = 0
                board[k] = " "
        if char == "O":
            if dic[k] == 10:
                dic[k] = 0
                board[k] = " "
