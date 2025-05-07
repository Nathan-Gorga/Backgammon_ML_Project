import tkinter as tk
from PIL import Image, ImageTk

import os
import tkinter as tk
from PIL import Image, ImageTk



script_dir = os.path.dirname(os.path.abspath(__file__))




# You need a background image of the board (800x400 or adjust sizes below)
BOARD_IMAGE_PATH = os.path.join(script_dir, './board_assets/board.png')


print("Board path:", BOARD_IMAGE_PATH)


BLACK_TOKEN_PATH = os.path.join(script_dir, '../gui_token/token_assets/black_token.png')
WHITE_TOKEN_PATH = os.path.join(script_dir, '../gui_token/token_assets/white_token.png')

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
POINT_POSITIONS = [
    # Coordinates for each of the 24 points (approximate example)
    # These are for placing tokens; you'll need to adjust them based on your board image
    (614, 365), (560, 365), (507, 365), (453, 365), (400, 365), (346, 365),
    (283, 365), (229, 365), (176, 365), (122, 365), (69, 365), (15, 365),
    (15, 25), (69, 25), (122, 25), (176, 25), (229, 25), (283, 25),
    (346, 25), (400, 25), (453, 25), (507, 25), (560, 25), (614, 25)
]

# Example token layout: (point index, color)
TOKENS = [
    (0, 'black'), (1, 'black'),(2, 'white'), (3, 'white'), (4, 'white'),(5, 'black'), 
    (6, 'black'), (7, 'black'),(8, 'white'), (9, 'white'), (10, 'white'),(11, 'black'),
    (12, 'black'), (13, 'black'),(14, 'white'), (15, 'white'), (16, 'white'),(17, 'black'),
    (18, 'black'), (19, 'black'),(20, 'white'), (21, 'white'), (22, 'white'),(23, 'black')
]

def draw_board_gui():
    root = tk.Tk()
    root.title("Backgammon GUI")
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    # Load images
    board_img = Image.open(BOARD_IMAGE_PATH)
    board_photo = ImageTk.PhotoImage(board_img)

    black_token_img = ImageTk.PhotoImage(Image.open(BLACK_TOKEN_PATH).resize((30, 30)))
    white_token_img = ImageTk.PhotoImage(Image.open(WHITE_TOKEN_PATH).resize((30, 30)))

    # Keep references
    canvas.board_photo = board_photo
    canvas.red_token_img = black_token_img
    canvas.white_token_img = white_token_img

    # Draw board
    canvas.create_image(0, 0, anchor=tk.NW, image=board_photo)

    # Draw tokens
    point_counters = {}  # Keep track of how many tokens are stacked per point

    for idx, color in TOKENS:
        x, y = POINT_POSITIONS[idx]
        count = point_counters.get(idx, 0)
        offset = count * 10 if idx < 12 else -count * 10  # stack vertically

        # Adjust y for stacking
        y_stack = y + offset if idx < 12 else y - offset

        token_img = black_token_img if color == 'black' else white_token_img
        canvas.create_image(x, y_stack, anchor=tk.NW, image=token_img)

        point_counters[idx] = count + 1

    root.mainloop()

if __name__ == "__main__":
    draw_board_gui()