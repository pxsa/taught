# tic-tac-tok  

# 1- game board
# 2- update game board

import os

board_lv1 = ["", "", ""]
board_lv2 = ["", "", ""]
board_lv3 = ["", "", ""]


def gameBoard():
    o_border = "----------------"
    i_border_lv1 = f"|  {board_lv1[0]}  |  {board_lv1[1]}  |  {board_lv1[2]}  |"
    i_border_lv2 = f"|  {board_lv2[0]}  |  {board_lv2[1]}  |  {board_lv2[2]}  |"
    i_border_lv3 = f"|  {board_lv3[0]}  |  {board_lv3[1]}  |  {board_lv3[2]}  |"
    game_board = f"{o_border}\n{i_border_lv1}\n{o_border}\n{i_border_lv2}\n{o_border}\n{i_border_lv3}\n{o_border}"
    print(game_board) 

def updateBoard(player, input):
    # i_border = f"| {} | {} | {} |"
    
    j = input % 3
    i = input // 3
    player_sign = "O" if player == "user1" else "X"

    if i == 0:
        if board_lv1[j] == "":
            board_lv1[j] = player_sign
    elif i == 1:
        if board_lv2[j] == "":
            board_lv2[j] = player_sign
    else:
        if board_lv3[j] == "":
            board_lv3[j] = player_sign


i = 0
while True:
    os.system("clear")
    gameBoard()
    userInput = int(input("Enter a position (1-9): "))   
    turn = "user1" if (i%2 == 0) else "user2" 
    i += 1
    updateBoard(turn, userInput-1)