
from re import A
import sys
import pygame
from colors import Colors
from snake import Snake
from apple import Apple
# from tile import Tile

pygame.init()

display = pygame.display
screen = display.set_mode((625, 625))

clock = pygame.time.Clock()
snake = Snake()
apple = Apple()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.move_direction = 'right'
            if event.key == pygame.K_LEFT:
                snake.move_direction = 'left'
            if event.key == pygame.K_UP:
                snake.move_direction = 'up'
            if event.key == pygame.K_DOWN:
                snake.move_direction = 'down'
        if event.type == GAME_UPDATE:
            snake.move()

    # Background
    screen.fill(Colors.green)

    # Drawing
    snake.draw(screen)
    apple.draw(screen)

    display.update()
    clock.tick(60)
