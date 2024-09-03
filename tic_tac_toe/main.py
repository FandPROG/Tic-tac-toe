import pygame
import sys
from drawing import *
from ai import *
from game import *

def show_difficulty_selection(screen, WIDTH, HEIGHT, draw_text, HIGHLIGHT, BLACK):
    global difficulty, selected_option
    selected_option = 1  # 기본값
    while True:
        screen.fill(WHITE)
        draw_text(screen, 'Select Difficulty:', BLACK, WIDTH // 4, HEIGHT // 3, 50)
        
        options = ['1. Easy', '2. Hard']
        for i, option in enumerate(options):
            option_x = WIDTH // 2 - 75
            option_y = HEIGHT // 2 - 25 + i * 50
            if i + 1 == selected_option:
                pygame.draw.rect(screen, HIGHLIGHT, (option_x - 10, option_y - 5, 150, 30))
            draw_text(screen, option, BLACK, option_x, option_y, 33)
        
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
    pygame.init()
    
    WIDTH, HEIGHT = 500, 500
    LINE_WIDTH = 25
    SQUARE_SIZE = WIDTH // 3
    CIRCLE_RADIUS = SQUARE_SIZE // 3
    CIRCLE_WIDTH = 25
    CROSS_WIDTH = 40
    SPACE = 50

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    HIGHLIGHT = (200, 200, 255)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe')

    board = [0] * 9
    player = 'x'
    difficulty = None
    selected_square = [0, 0]
    game_over = False

    show_difficulty_selection(screen, WIDTH, HEIGHT, draw_text, HIGHLIGHT, BLACK)
    
    draw_board(screen, WIDTH, HEIGHT, SQUARE_SIZE, LINE_WIDTH, BLACK, WHITE)
    draw_shapes(screen, board, lambda x, y: draw_x(screen, x, y, SQUARE_SIZE, SPACE, CROSS_WIDTH, RED),
                        lambda x, y: draw_o(screen, x, y, SQUARE_SIZE, CIRCLE_RADIUS, CIRCLE_WIDTH, BLUE))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_square[1] = (selected_square[1] - 1) % 3
                elif event.key == pygame.K_DOWN:
                    selected_square[1] = (selected_square[1] + 1) % 3
                elif event.key == pygame.K_LEFT:
                    selected_square[0] = (selected_square[0] - 1) % 3
                elif event.key == pygame.K_RIGHT:
                    selected_square[0] = (selected_square[0] + 1) % 3
                elif event.key == pygame.K_RETURN and not game_over:
                    x, y = selected_square
                    if board[y * 3 + x] == 0:
                        board[y * 3 + x] = 1
                        draw_x(screen, x, y, SQUARE_SIZE, SPACE, CROSS_WIDTH, RED)
                        player = 'o'
                        pygame.display.update()

                        winner = is_winner(board)
                        if winner:
                            game_over = True
                            result_text = "Player Wins!" if winner == 1 else "AI Wins!"
                            draw_board(screen, WIDTH, HEIGHT, SQUARE_SIZE, LINE_WIDTH, BLACK, WHITE)
                            draw_shapes(screen, board, lambda x, y: draw_x(screen, x, y, SQUARE_SIZE, SPACE, CROSS_WIDTH, RED),
                                            lambda x, y: draw_o(screen, x, y, SQUARE_SIZE, CIRCLE_RADIUS, CIRCLE_WIDTH, BLUE))
                            draw_text(screen, result_text, BLACK, WIDTH // 4, HEIGHT // 2, 50)
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
                                ai_row, ai_col = move // 3, move % 3
                                draw_o(screen, ai_col, ai_row, SQUARE_SIZE, CIRCLE_RADIUS, CIRCLE_WIDTH, BLUE)
                                pygame.display.update()

                                winner = is_winner(board)
                                if winner:
                                    game_over = True
                                    result_text = "Player Wins!" if winner == 1 else "AI Wins!"
                                    draw_board(screen, WIDTH, HEIGHT, SQUARE_SIZE, LINE_WIDTH, BLACK, WHITE)
                                    draw_shapes(screen, board, lambda x, y: draw_x(screen, x, y, SQUARE_SIZE, SPACE, CROSS_WIDTH, RED),
                                                    lambda x, y: draw_o(screen, x, y, SQUARE_SIZE, CIRCLE_RADIUS, CIRCLE_WIDTH, BLUE))
                                    draw_text(screen, result_text, BLACK, WIDTH // 4, HEIGHT // 2, 50)
                                    pygame.display.update()
                                    pygame.time.delay(2000)
                                    pygame.quit()
                                    sys.exit()

                                player = 'x'
                                if not is_empty(board) and not game_over:
                                    result_text = "DRAW!"
                                    game_over = True
                                    draw_board(screen, WIDTH, HEIGHT, SQUARE_SIZE, LINE_WIDTH, BLACK, WHITE)
                                    draw_shapes(screen, board, lambda x, y: draw_x(screen, x, y, SQUARE_SIZE, SPACE, CROSS_WIDTH, RED),
                                                    lambda x, y: draw_o(screen, x, y, SQUARE_SIZE, CIRCLE_RADIUS, CIRCLE_WIDTH, BLUE))
                                    draw_text(screen, result_text, BLACK, WIDTH // 4, HEIGHT // 2, 50)
                                    pygame.display.update()
                                    pygame.time.delay(2000)
                                    pygame.quit()
                                    sys.exit()

        draw_board(screen, WIDTH, HEIGHT, SQUARE_SIZE, LINE_WIDTH, BLACK, WHITE)
        draw_shapes(screen, board, lambda x, y: draw_x(screen, x, y, SQUARE_SIZE, SPACE, CROSS_WIDTH, RED),
                        lambda x, y: draw_o(screen, x, y, SQUARE_SIZE, CIRCLE_RADIUS, CIRCLE_WIDTH, BLUE))
        draw_selected_square(screen, selected_square, SQUARE_SIZE, GREEN)
        pygame.display.update()

if __name__ == "__main__":
    main()
