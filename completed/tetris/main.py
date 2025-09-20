import sys
import pygame
from game import Game
from colors import Colors

pygame.init()

DISPLAY = pygame.display
SCREEN = DISPLAY.set_mode((500, 620))


def text(value, coordinates, rect=pygame.rect.RectType, centered=False,):
    font = pygame.font.Font(None, 40)
    text = font.render(value, True, Colors.WHITE)
    if not centered:
        SCREEN.blit(text, coordinates)
    else:
        SCREEN.blit(text, text.get_rect(
            centerx=rect.centerx, centery=rect.centery))


def rect(left, top, width, height):
    rect = pygame.Rect(left, top, width, height)
    return pygame.draw.rect(SCREEN, Colors.LIGHT_BG, rect, 0, 10)


clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, game.game_speed)

# Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and not game.game_over:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                # game.update_score(0, 1)
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
        elif event.type == pygame.KEYDOWN and game.game_over:
            game.game_over = False
            game.reset()

        if event.type == GAME_UPDATE and not game.game_over:
            pygame.time.set_timer(GAME_UPDATE, game.game_speed)
            game.move_down()

    # Drawing
    SCREEN.fill(Colors.BG)
    text('Score', (365, 20, 50, 50))
    score_rect = rect(320, 55, 170, 60)
    text(f'{game.score}', None, rect=score_rect, centered=True)

    text('Next', (375, 180, 50, 50))
    next_rect = rect(320, 215, 170, 180)

    if game.game_over:
        text('GAME OVER', (320, 450, 50, 50))
    game.draw(SCREEN)

    DISPLAY.update()
    clock.tick(60)
