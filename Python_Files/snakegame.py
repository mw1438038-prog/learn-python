import pygame
import random

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
green = (0, 255, 0)
dark_green = (0, 100, 0)
red = (255, 0, 0)
black = (0, 0, 0)

snake_block = 10
snake_speed = 5

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# 🔹 Score
def show_score(score):
    value = font.render("Score: " + str(score), True, black)
    screen.blit(value, [10, 10])

# 🔹 Snake draw (with face)
def draw_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):

        # Head
        if i == len(snake_list) - 1:
            pygame.draw.rect(screen, dark_green, [x[0], x[1], snake_block, snake_block])

            # Eyes 👀
            pygame.draw.rect(screen, white, [x[0] + 2, x[1] + 2, 2, 2])
            pygame.draw.rect(screen, white, [x[0] + 6, x[1] + 2, 2, 2])

        else:
            # Body
            pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# 🔹 Message
def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length = 1
    score = 0

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message("Game Over! Q-Quit C-Play Again", red)
            show_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        break
                    if event.key == pygame.K_c:
                        gameLoop()
                        break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        x += x_change
        y += y_change

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        screen.fill(white)

        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
                break

        draw_snake(snake_block, snake_list)

        show_score(score)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1
            score += 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()