import time
import pygame
import random
import os

pygame.init()

#define colors

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
green = (0, 128, 0)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#clock

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 20)

score_font = pygame.font.SysFont('ubuntu', 15)

clock_font = pygame.font.SysFont('arial', 15)

#functions

def print_score(score):
    text = score_font.render("Score: " + str(score), True, white)
    game_display.blit(text, [10, 10])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, green, [pixel[0], pixel[1], snake_size, snake_size])
        
def run_game():
    game_over = False
    game_close = False

    x = width/2
    y = height/2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1
    
    target_x = round(random.randrange(10, width - snake_size - 10) / 10) * 10
    target_y = round(random.randrange(10, height - snake_size - 10) / 10) * 10

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("""Game Over!""", True, red)
            cmd_message = message_font.render("Press 1 to quit, 2 to play again", True, red)
            game_over_rect = game_over_message.get_rect(center=(width/2, height/3))
            cmd_message_rect = cmd_message.get_rect(center = (width/2, height/2))
            game_display.blit(game_over_message, game_over_rect)
            game_display.blit(cmd_message, cmd_message_rect)
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        return True  # Return True to indicate restarting the game
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if x_speed == snake_size:
                        x_speed == snake_size
                    else:
                        x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if x_speed == -snake_size:
                        x_speed = -snake_size
                    else:
                        x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    x_speed = 0
                    if y_speed == snake_size:
                        y_speed = snake_size
                    else:
                        y_speed = -snake_size
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    x_speed = 0
                    if y_speed == -snake_size:
                        y_speed = -snake_size
                    else:
                        y_speed = snake_size
                if event.key == pygame.K_ESCAPE:
                    game_close = False
                    game_over = True
                global snake_speed
                if event.key == pygame.K_p:
                    snake_speed = 45
                if event.key == pygame.K_o:
                    snake_speed = 15
                    
        pygame.display.update()

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)

        pygame.draw.rect(game_display, red, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                pass
                # game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(10, width - snake_size - 10) / 10) * 10
            target_y = round(random.randrange(10, height - snake_size - 10) / 10) * 10
            snake_length += 1

        clock.tick(snake_speed)
        pygame.display.update()

    return False  # Return False to indicate quitting the game

# Run the game loop

while run_game():
    
    pass  # Continue running the game as long as run_game returns True

pygame.quit()
os._exit()