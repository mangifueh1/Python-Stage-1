import sys
import pygame
from colors import Colors
from game import Game

pygame.init()

display = pygame.display
screen = display.set_mode((625, 625))
display.set_caption('Snake Game')

clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 100)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                game.change_direction('right')
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                game.change_direction('left')
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                game.change_direction('up')
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                game.change_direction('down')
            if event.key == pygame.K_ESCAPE:
                game.pause()
        if event.type == GAME_UPDATE and not game.game_over and not game.paused:
            game.move()
            game.is_game_end()
            if game.is_collision():
                game.score += 1
                game.apple.move()
                game.extend_snake()
            game.is_body()
        if event.type == pygame.KEYDOWN and game.game_over:
            game.reset()

    # Background
    screen.fill(Colors.green)

    # Drawing

    game.draw(screen)
    if not game.game_over:
        game.text(f'Score: {game.score}', (10, 10), 30, screen)
        if game.paused:
            game.text('Game Paused',
                      (0, 0), 50, screen, centered=True)
    else:
        game.text(f'Game Over: {game.score}',
                  (0, 0), 50, screen, centered=True)

    display.update()
    clock.tick(60)
