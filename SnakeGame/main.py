import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for x in snake_list:
            pygame.draw.rect(screen, WHITE, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


gameLoop()
