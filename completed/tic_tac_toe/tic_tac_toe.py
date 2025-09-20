from time import sleep
import tkinter as tk
import random

ROWS = 3
COLS = 3
TILE_SIZE = 250
WIN_METHODS = (['tl', 'cl', 'bl'], ['tc', 'cc', 'bc'], ['tr', 'cr', 'br'], ['tl', 'tc', 'tr'],
               ['cl', 'cc', 'cr'], ['bl', 'bc', 'br'], ['tl', 'cc', 'br'], ['tr', 'cc', 'bl'])

WINDOW_HEIGHT = TILE_SIZE * ROWS
WINDOW_WIDTH = TILE_SIZE * COLS


class Tile:
    def __init__(self, x, y, val):
        self.col = x
        self.row = y
        self.val = val


window = tk.Tk()
window.title('Tic-Tac-Toe')
window.resizable(False, False)

canvas = tk.Canvas(master=window, bg='white', width=WINDOW_WIDTH,
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

against_ai = True
player_turn = True
player_symbol = 'x'
ai_symbol = 'o'


def reset():
    global current_sym, game_over, x_spaces, o_spaces, previous_sym, ai_spaces, result

    current_sym = 'o'
    previous_sym = 'x'
    game_over = False
    x_spaces = []
    o_spaces = []
    ai_spaces = []
    # used_spaces = []
    result = f'{previous_sym}\' Wins'


def color():

    if current_sym == 'o':
        return 'green'
    else:
        return 'red'


def get_location(row, col):
    # Top Left
    if row == 0 and col == 0:
        return 'tl'
    # Center Left
    elif row == 0 and col == 1:
        return 'cl'
    # Bottom Left
    elif row == 0 and col == 2:
        return 'bl'

    # Top Center
    elif row == 1 and col == 0:
        return 'tc'
    # Center Center
    elif row == 1 and col == 1:
        return 'cc'
    # Bottom Center
    elif row == 1 and col == 2:
        return 'bc'

    # Top Right
    elif row == 2 and col == 0:
        return 'tr'
    # Center Right
    elif row == 2 and col == 1:
        return 'cr'
    # Bottom Right
    elif row == 2 and col == 2:
        return 'br'


def show_symbol(e):
    global current_sym
    # print(e)

    if game_over == True:
        return

    posX = e.x
    posY = e.y

    # Switch symbol and append space to list
    def symbol_controller(space):
        global current_sym, previous_sym

        if against_ai:
            if current_sym == player_symbol:
                current_sym = ai_symbol
                previous_sym = player_symbol
                o_spaces.append(space)
            else:
                current_sym = player_symbol
                previous_sym = ai_symbol
                ai_spaces.append(space)
        else:
            if current_sym == 'x':
                current_sym = 'o'
                previous_sym = 'x'
                x_spaces.append(space)
            else:
                current_sym = 'x'
                previous_sym = 'o'
                o_spaces.append(space)

    # AI for singe player
    def ai_model():
        global player_turn, current_sym, previous_sym

        row = random.randint(0, ROWS-1)
        col = random.randint(0, COLS-1)
        space = get_location(row, col)

        if game_over:
            pass
        else:
            if not player_turn:
                if space in ai_spaces or space in o_spaces:
                    canvas.after(100, ai_model)
                else:
                    symbol_controller(space)
                    canvas.create_text(((2*(row) + 1)*TILE_SIZE) / 2, ((2*(col) + 1)*TILE_SIZE - 50) / 2,
                                       text=current_sym, font='Calibri 200', fill=color(), tags='sym')
                    player_turn = True
            else:
                pass

        return 'AI'

    def use_space(row, col,):
        global previous_sym, current_sym, player_turn

        space = get_location(row, col)

        if space in x_spaces or space in o_spaces:
            pass
        else:
            if player_turn:
                symbol_controller(space)
                canvas.create_text(((2*(row) + 1)*TILE_SIZE) / 2, ((2*(col) + 1)*TILE_SIZE - 50) / 2,
                                   text=current_sym, font='Calibri 200', fill=color(), tags='sym')
                if against_ai:
                    player_turn = False
                else:
                    pass
            else:
                pass

    for row in range(ROWS):
        for col in range(COLS):
            if posX in range((0 + row)*TILE_SIZE, (1 + row)*TILE_SIZE) and posY in range((0 + col)*TILE_SIZE, (1 + col)*TILE_SIZE):

                # Top Left
                if row == 0 and col == 0:
                    use_space(row, col)
                # Center Left
                elif row == 0 and col == 1:
                    use_space(row, col)
                # Bottom Left
                elif row == 0 and col == 2:
                    use_space(row, col)

                # Top Center
                elif row == 1 and col == 0:
                    use_space(row, col)
                # Center Center
                elif row == 1 and col == 1:
                    use_space(row, col)
                # Bottom Center
                elif row == 1 and col == 2:
                    use_space(row, col)

                # Top Right
                elif row == 2 and col == 0:
                    use_space(row, col)
                # Center Right
                elif row == 2 and col == 1:
                    use_space(row, col)
                # Bottom Right
                elif row == 2 and col == 2:
                    use_space(row, col)

                if against_ai:
                    canvas.after(2000, ai_model)
                else:
                    pass

                # used_spaces.append((row, col))
    # print(used_spaces)


def create_grid():
    # global mouse_location
    canvas.delete('turn')
    for row in range(ROWS):
        for col in range(COLS):
            box = Tile(col*TILE_SIZE, row*TILE_SIZE, current_sym)

            canvas.create_rectangle(
                box.col,
                box.row,
                box.col + TILE_SIZE,
                box.row + TILE_SIZE,
                outline='black'
            )

    if not game_over:
        canvas.create_text(
            50, 20, text=f'{previous_sym}\' turns', fill='black', font='Calibri 20', tags='turn')
    else:
        canvas.create_text(window_height/2, window_width /
                           2, text=result, fill='grey', font='Calibri 40',)


def check_win():
    global x_spaces, o_spaces, game_over, current_sym, result

    if against_ai:
        for method in WIN_METHODS:
            if set(method).issubset(o_spaces):
                game_over = True
            elif set(method).issubset(ai_spaces):
                game_over = True
    else:
        for method in WIN_METHODS:
            if set(method).issubset(x_spaces):
                game_over = True
            elif set(method).issubset(o_spaces):
                game_over = True

    if game_over == True:
        canvas.after_cancel('AI')
        canvas.delete('turn')

    if len(x_spaces + o_spaces) == 9 or len(ai_spaces + o_spaces) == 9:
        result = 'Draw'
        game_over = True


def draw():
    check_win()
    create_grid()
    canvas.create_rectangle(0, window_height-30, window_width,
                            window_height, fill='black')
    if against_ai:
        canvas.create_text(window_width/2, window_height-15,
                           text='Player VS CPU', fill='white', font='courier 15 bold')
    else:
        canvas.create_text(window_width/2, window_height-15,
                           text='Player VS Player', fill='white', font='courier 15 bold')

    canvas.after(100, draw)


reset()
draw()


window.bind('<Button-1>', show_symbol)
window.mainloop()
