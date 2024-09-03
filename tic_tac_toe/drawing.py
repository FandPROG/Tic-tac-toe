import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (200, 200, 255)

def draw_board(screen, WIDTH, HEIGHT, SQUARE_SIZE, LINE_WIDTH, BLACK, WHITE):
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_x(screen, x, y, SQUARE_SIZE, SPACE, CROSS_WIDTH, RED):
    pygame.draw.line(screen, RED, (x * SQUARE_SIZE + SPACE, y * SQUARE_SIZE + SPACE),
                     ((x + 1) * SQUARE_SIZE - SPACE, (y + 1) * SQUARE_SIZE - SPACE), CROSS_WIDTH)
    pygame.draw.line(screen, RED, ((x + 1) * SQUARE_SIZE - SPACE, y * SQUARE_SIZE + SPACE),
                     (x * SQUARE_SIZE + SPACE, (y + 1) * SQUARE_SIZE - SPACE), CROSS_WIDTH)

def draw_o(screen, x, y, SQUARE_SIZE, CIRCLE_RADIUS, CIRCLE_WIDTH, BLUE):
    pygame.draw.circle(screen, BLUE, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2),
                       CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_shapes(screen, board, draw_x, draw_o):
    for row in range(3):
        for col in range(3):
            if board[row * 3 + col] == 1:
                draw_x(col, row)
            elif board[row * 3 + col] == 2:
                draw_o(col, row)

def draw_selected_square(screen, selected_square, SQUARE_SIZE, GREEN):
    x, y = selected_square
    pygame.draw.rect(screen, GREEN, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

def draw_text(screen, text, color, x, y, size):
    font = pygame.font.SysFont(None, size)
    label = font.render(text, True, color)
    screen.blit(label, (x, y))
