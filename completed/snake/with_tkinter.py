import tkinter as tk
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_HEIGHT = TILE_SIZE * ROWS
WINDOW_WIDTH = TILE_SIZE * COLS


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


window = tk.Tk()
window.title('Snake')
window.resizable(False, False)

canvas = tk.Canvas(master=window, bg='green', width=WINDOW_WIDTH,
                   height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()


window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(
    f"{window_width}x{window_height}+{window_x}+{window_y}")


def reset():
    global snake, food, velocityX, velocityY, snake_body, game_over, score

    snake = Tile(random.randint(0, COLS-1) * TILE_SIZE,
                 random.randint(0, ROWS-1) * TILE_SIZE)
    food = Tile(random.randint(0, COLS-1) * TILE_SIZE,
                random.randint(0, ROWS-1) * TILE_SIZE)
    velocityX = 0
    velocityY = 0
    snake_body = []
    game_over = False
    score = 0


def change_direction(e):
    key = e.keysym
    global velocityY, velocityX
    # print(key)
    if game_over:
        if key == 'space':
            reset()
        return

    if key == 'Left' and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif key == 'Right' and velocityX != -1:
        velocityX = 1
        velocityY = 0
    elif key == 'Up' and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif key == 'Down' and velocityY != -1:
        velocityX = 0
        velocityY = 1


def move():
    global snake, food, snake_body, game_over, score

    if game_over:
        return

    if snake.x < 0 or snake.y < 0 or snake.x >= WINDOW_WIDTH or snake.y >= WINDOW_HEIGHT:
        game_over = True
        return

    for tile in snake_body:
        if tile.x == snake.x and tile.y == snake.y:
            game_over = True
            return

    # Handle Collision
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1

    # Update Snake Body
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if i == 0:
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

# Draw on canvas


def draw():
    global snake, food, snake_body, game_over
    move()
    canvas.delete('all')

    canvas.create_rectangle(food.x, food.y, food.x +
                            TILE_SIZE, food.y + TILE_SIZE, fill='red', outline='red')
    canvas.create_rectangle(snake.x, snake.y, snake.x +
                            TILE_SIZE, snake.y + TILE_SIZE, fill='yellow',)

    for tile in snake_body:
        canvas.create_rectangle(
            tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill='yellow', outline='yellow')

    if game_over:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT /
                           2, text=f'Game Over: {score}', fill='white', font='Arial 20')
    else:
        canvas.create_text(
            40, 20, text=f'Points: {score}', fill='white', font='Arial 10')

    canvas.after(100, draw)


reset()
draw()

window.bind('<KeyRelease>', change_direction)
window.mainloop()
