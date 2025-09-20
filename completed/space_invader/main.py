from math import sqrt
from random import choice, randint, randrange
import pygame

pygame.init()

DISPLAY = pygame.display
SCREEN = DISPLAY.set_mode((800, 600))
DISPLAY.set_caption('Space Invaders')
WINDOW_WIDTH = DISPLAY.get_window_size()[0]
WINDOW_HEIGHT = DISPLAY.get_window_size()[1]
ENEMY_SPEED = 0.8
PLAYER_SPEED = 1.5


def iload(src):
    return pygame.image.load(src)


class Enemy:
    def __init__(self, index, state='show',):
        global enemies, enemy_number

        self.IMG = iload('space_invader/enemy.png')
        self.width = self.IMG.get_width()
        self.height = self.IMG.get_height()
        self.X = randrange(
            0, (WINDOW_WIDTH - self.width), self.width)
        self.Y = randrange((int((enemy_number/2))*-self.height),
                           (-self.height), self.height)
        self.velocityX = choice((-ENEMY_SPEED, ENEMY_SPEED))
        self.velocityY = .27
        self.state = state
        self.index = index

    def show(self):
        # self.state = 'show'
        global score
        if self.X <= 0:
            self.velocityX = ENEMY_SPEED
        elif self.X > (WINDOW_WIDTH - self.width):
            self.velocityX = -ENEMY_SPEED

        self.Y += self.velocityY
        self.X += self.velocityX
        if self.state == 'show':
            SCREEN.blit(self.IMG, (self.X, self.Y))
        elif self.state == 'hide':
            self.IMG = None
            self.X = WINDOW_WIDTH + 10
            self.Y = 0


class Bullet:
    def __init__(self, state='ready',):
        global player

        self.IMG = iload('space_invader/bullet.png')
        self.width = self.IMG.get_width()
        self.height = self.IMG.get_height()
        self.X = player.X
        self.Y = player.Y
        self.velocityX = 0
        self.velocityY = -10
        self.state = state

    def fire(self, x, y):
        self.state = 'fire'
        SCREEN.blit(self.IMG, (x + player.width/2, y))


class Player:
    def __init__(self):
        self.IMG = iload('space_invader/ship.png')
        self.width = self.IMG.get_width()
        self.X = (WINDOW_WIDTH / 2) - (self.width / 2)
        self.Y = WINDOW_HEIGHT - 100
        self.velocityX = 0

    def move(self):

        if self.X < 0:
            self.X = 0
        elif self.X > (WINDOW_WIDTH - self.width):
            self.X = (WINDOW_WIDTH - self.width)

        self.X += self.velocityX
        SCREEN.blit(self.IMG, (self.X, self.Y))


game_over = False

score = 0
font = pygame.font.Font('freesansbold.ttf', 20)
scoreX = 10
scoreY = 10


def show_score():
    show_text = font.render(f'Score: {score}', True, (255, 255, 255))
    SCREEN.blit(show_text, (scoreX, scoreY))


def show_splash():
    global enemy_left
    if not game_over:
        text = font.render(
            'SPACE INVADERS: Press "Enter" to start', True, (255, 255, 255))
        x = (WINDOW_WIDTH / 2) - (text.get_width()/2)
        y = WINDOW_HEIGHT / 2
        SCREEN.blit(text, (x, y))
    elif game_over and enemy_left == 0:
        text = font.render(
            'GAME OVER: YOU COMPLETED THE MISSION', True, (255, 255, 255))
        x = (WINDOW_WIDTH / 2) - (text.get_width()/2)
        y = WINDOW_HEIGHT / 2
        SCREEN.blit(text, (x, y))
    elif game_over and enemy_left > 0:
        text = font.render(
            f'GAME OVER: {score}', True, (255, 255, 255))
        x = (WINDOW_WIDTH / 2) - (text.get_width()/2)
        y = WINDOW_HEIGHT / 2
        SCREEN.blit(text, (x, y))


# Initialize Player
player = Player()

# Initialize Enemy
enemies = []
enemy_number = 20
enemy_left = enemy_number
for i in range(enemy_number):
    enemy = Enemy(index=i)
    enemies.append(enemy)


# initialize Bullet
bullet = Bullet()


def is_collision(x1, y1, x2, y2):
    global enemy_left

    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if distance <= 60:
        enemy_left -= 1
        return True
    else:
        return False


background = iload('space_invader/background.png')


# Keep program running
running = True
splash = True

while running:
    SCREEN.fill((0, 0, 0))
    if splash:
        pass
    else:
        SCREEN.blit(background, (0, 0))

    for event in pygame.event.get():

        # For Closing program
        if event.type == pygame.QUIT:
            splash = False
            running = False

        # Arrow keys pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.velocityX = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                player.velocityX = PLAYER_SPEED
            elif event.key == pygame.K_SPACE:
                bullet.X = player.X
                bullet.fire(bullet.X, bullet.Y)
            elif event.key == pygame.K_RETURN:
                splash = False

        # Arrow keys released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.velocityX = 0

    if not splash:
        if bullet.Y <= 0:
            bullet.state = 'ready'
            bullet.Y = player.Y
        if bullet.state == 'fire':
            bullet.fire(bullet.X, bullet.Y)
            bullet.Y += bullet.velocityY

        for i in range(enemy_number):
            enemies[i].show()
            if is_collision(enemies[i].X, enemies[i].Y, bullet.X, bullet.Y):
                bullet.Y = player.Y
                bullet.state = 'ready'
                enemies[i].state = 'hide'
                score += 1
            elif (enemies[i].Y + enemies[i].height) - player.Y > 0:
                game_over = True
                splash = True

        if score == enemy_number:
            splash = True
            game_over = True

        show_score()
        player.move()
    else:
        show_splash()

    # Keed updating display
    DISPLAY.update()
