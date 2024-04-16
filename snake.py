import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# game window
window = tkinter.Tk()
window.title("Snake")
window.resizable = (False, False)


canvas = tkinter.Canvas(
    window,
    bg="black",
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    borderwidth=0,
    highlightthickness=0,
)
canvas.pack()
window.update()

# Center window on screen
win_w = window.winfo_width()
win_h = window.winfo_height()
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()

win_x = int((screen_w / 2) - (win_w / 2))
win_y = int((screen_h / 2) - (win_h / 2))

window.geometry(f"{win_w}x{win_h}+{win_x}+{win_y}")


# initialise game
# snakes head
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
food = Tile(10 * TILE_SIZE, 15 * TILE_SIZE)
snake_body = []
velX = 0
velY = 0


def change_dir(e):
    global velX, velY

    if e.keysym == "Up" and velY != 1:
        velX = 0
        velY = -1
    elif e.keysym == "Down" and velY != -1:
        velX = 0
        velY = 1
    elif e.keysym == "Left" and velX != 1:
        velX = -1
        velY = 0
    elif e.keysym == "Right" and velX != -1:
        velX = 1
        velY = 0


def move():
    global snake

    # collision
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE

    snake.x += velX * TILE_SIZE
    snake.y += velY * TILE_SIZE


def draw():
    global snake
    move()
    canvas.delete("all")

    #  draw food
    canvas.create_rectangle(
        food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="blue"
    )
    # draw snake
    canvas.create_rectangle(
        snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="#e619a2"
    )

    for tile in snake_body:
        canvas.create_rectangle(
            tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="#e619a2"
        )

    window.after(100, draw)
    # 10 fps


draw()
window.bind("<KeyRelease>", change_dir)
window.mainloop()
