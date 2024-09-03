import random
from game import *

def easy_AI(board):
    while True:
        ran = random.randrange(0, 9)
        if board[ran] == 0:
            return ran

def MiniMax(player, brd):
    winner = is_winner(brd)

    if winner == 2:  
        return -1, 1
    elif winner == 1:  
        return -1, -1
    elif not is_empty(brd):  
        return -1, 0

    if player == 2:  
        mx = -2e9
        best_move = -1
        for i in range(9):
            if brd[i] == 0:
                brd[i] = 2
                move, m = MiniMax(1, brd)
                brd[i] = 0
                if m > mx:
                    mx = m
                    best_move = i
        return best_move, mx
    else:  
        mn = 2e9
        best_move = -1
        for i in range(9):
            if brd[i] == 0:
                brd[i] = 1
                move, m = MiniMax(2, brd)
                brd[i] = 0
                if m < mn:
                    mn = m
                    best_move = i
        return best_move, mn
