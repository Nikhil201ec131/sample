# tic tak toe;
print("let's play tic|tok|toe\n")
board = [" _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "]


def board_display():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


board_display()


def winner(p):
    #row winner
    if ((board[0] == board[1] == board[2] != " _ ")
            or (board[3] == board[4] == board[5] != " _ ")
            or (board[6] == board[7] == board[8] != " _ ")):
        print("player-", p, " is the winner completing a row ")
        return True
    # column winner
    if ((board[0] == board[3] == board[6] != " _ ")
            or (board[1] == board[4] == board[7] != " _ ")
            or (board[2] == board[5] == board[8] != " _ ")):
        print("player-", p, " is the winner completing a column ")
        return True
    #diagnal winner
    if ((board[0] == board[4] == board[8] != " _ ")
            or (board[2] == board[4] == board[6] != " _ ")):
        print("player-", p, " is the winner completing a diagnal ")
        return True
    if " _ " not in board:
        print("The game up is 'TIE' ")
        return True


Game = True

while (Game):
    player_1_input = input("player 1 : select your position from 1 to 9 :")
    x = int(player_1_input)
    if x not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        x = int(
            input("invalid input.enter correct input\n enter a new input:"))
    if board[x - 1] in [" X ", " 0 "]:
        x = int(
            input("this position is already occupied enter other position:"))
    board[x - 1] = " X "
    board_display()
    if (winner(1) == True):
        break
    # player 2 input
    player_2_input = input("player 2 : select your position from 1 to 9 :")
    y = int(player_2_input)
    if y not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        y = int(
            input("invalid input.enter correct input\n enter a new input:"))
    if board[y - 1] in [" X ", " 0 "]:
        y = int(
            input("this position is already occupied enter other position:"))
    board[y - 1] = " 0 "
    board_display()
    if (winner(0) == True):
        break

print("GAME OVER")
