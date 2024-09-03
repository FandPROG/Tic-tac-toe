import pygame
import random
import sys

pygame.init()

# 설정
WIDTH, HEIGHT = 1500, 1500
LINE_WIDTH = 75
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 75
CROSS_WIDTH = 125
SPACE = 150

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (200, 200, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

font = pygame.font.SysFont(None, 275)
small_font = pygame.font.SysFont(None, 100)
game_over = False

board = [0] * 9
player = 'x'
difficulty = None
selected_square = [0, 0]
selected_option = 1  # 전역 변수로 이동

def draw_board():
    screen.fill(WHITE)
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_x(x, y):
    pygame.draw.line(screen, RED, (x * SQUARE_SIZE + SPACE, y * SQUARE_SIZE + SPACE),
                     ((x + 1) * SQUARE_SIZE - SPACE, (y + 1) * SQUARE_SIZE - SPACE), CROSS_WIDTH)
    pygame.draw.line(screen, RED, ((x + 1) * SQUARE_SIZE - SPACE, y * SQUARE_SIZE + SPACE),
                     (x * SQUARE_SIZE + SPACE, (y + 1) * SQUARE_SIZE - SPACE), CROSS_WIDTH)

def draw_o(x, y):
    pygame.draw.circle(screen, BLUE, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2),
                       CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_shapes():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row * BOARD_COLS + col] == 1:
                draw_x(col, row)
            elif board[row * BOARD_COLS + col] == 2:
                draw_o(col, row)

def draw_selected_square():
    x, y = selected_square
    pygame.draw.rect(screen, GREEN, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 10)

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

def draw_text(text, color, x, y, size):
    font = pygame.font.SysFont(None, size)
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def show_difficulty_selection():
    global difficulty, selected_option
    selected_option = 1  # 기본값
    while True:
        screen.fill(WHITE)
        draw_text('Select Difficulty:', BLACK, WIDTH // 4, HEIGHT // 3, 150)
        
        options = ['1. Easy', '2. Hard']
        for i, option in enumerate(options):
            option_x = WIDTH // 2 - 150
            option_y = HEIGHT // 2 - 50 + i * 100
            if i + 1 == selected_option:
                pygame.draw.rect(screen, HIGHLIGHT, (option_x - 20, option_y - 10, 300, 60))
            draw_text(option, BLACK, option_x, option_y, 100)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = 1
                elif event.key == pygame.K_DOWN:
                    selected_option = 2
                elif event.key == pygame.K_RETURN:
                    difficulty = selected_option
                    return

def main():
    global player, difficulty, selected_square, game_over
    show_difficulty_selection()
    
    draw_board()
    draw_shapes()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_square[1] = (selected_square[1] - 1) % BOARD_ROWS
                elif event.key == pygame.K_DOWN:
                    selected_square[1] = (selected_square[1] + 1) % BOARD_ROWS
                elif event.key == pygame.K_LEFT:
                    selected_square[0] = (selected_square[0] - 1) % BOARD_COLS
                elif event.key == pygame.K_RIGHT:
                    selected_square[0] = (selected_square[0] + 1) % BOARD_COLS
                elif event.key == pygame.K_RETURN and not game_over:
                    x, y = selected_square
                    if board[y * BOARD_COLS + x] == 0:
                        board[y * BOARD_COLS + x] = 1
                        draw_x(x, y)
                        player = 'o'
                        pygame.display.update()

                        winner = is_winner(board)
                        if winner:
                            game_over = True
                            if winner == 1:
                                result_text = "Player Wins!"
                            elif winner == 2:
                                result_text = "AI Wins!"
                            draw_board()
                            draw_shapes()
                            draw_text(result_text, BLACK, WIDTH // 6, HEIGHT // 2, 275)
                            pygame.display.update()
                            pygame.time.delay(2000)
                            pygame.quit()
                            sys.exit()

                        if is_empty(board) and not game_over:
                            if player == 'o':
                                if difficulty == 1:
                                    move = easy_AI(board)
                                else:
                                    move, _ = MiniMax(2, board)
                                board[move] = 2
                                ai_row, ai_col = move // BOARD_COLS, move % BOARD_COLS
                                draw_o(ai_col, ai_row)
                                pygame.display.update()

                                winner = is_winner(board)
                                if winner:
                                    game_over = True
                                    if winner == 1:
                                        result_text = "Player Wins!"
                                    elif winner == 2:
                                        result_text = "AI Wins!"
                                    draw_board()
                                    draw_shapes()
                                    draw_text(result_text, BLACK, WIDTH // 6, HEIGHT // 2, 275)
                                    pygame.display.update()
                                    pygame.time.delay(2000)
                                    pygame.quit()
                                    sys.exit()

                                player = 'x'
                                if not is_empty(board) and not game_over:
                                    result_text = "DRAW!"
                                    game_over = True
                                    draw_board()
                                    draw_shapes()
                                    draw_text(result_text, BLACK, WIDTH // 3, HEIGHT // 2, 275)
                                    pygame.display.update()
                                    pygame.time.delay(2000)
                                    pygame.quit()
                                    sys.exit()

        draw_board()
        draw_shapes()
        draw_selected_square()
        pygame.display.update()

if __name__ == "__main__":
    main()
