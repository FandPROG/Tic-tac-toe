# game_logic.py

def is_winner(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                      (0, 4, 8), (2, 4, 6)]             
    for i in win_conditions:
        a, b, c = i
        if board[a] == board[b] == board[c] and board[a] != 0:
            return board[a]
    return 0

def is_empty(board):
    return 0 in board
