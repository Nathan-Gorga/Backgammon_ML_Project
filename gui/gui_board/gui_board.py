import tkinter as tk
from PIL import Image, ImageTk

import os
import tkinter as tk
from PIL import Image, ImageTk



script_dir = os.path.dirname(os.path.abspath(__file__))




# You need a background image of the board (800x400 or adjust sizes below)
BOARD_IMAGE_PATH = os.path.join(script_dir, './board_assets/board.png')

print("Board path:", BOARD_IMAGE_PATH)


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400
POINT_POSITIONS = [
    # Coordinates for each of the 24 points (approximate example)
    # These are for placing tokens; you'll need to adjust them based on your board image
    (619, 365), (565, 365), (512, 365), (458, 365), (405, 365), (351, 365),
    (288, 365), (234, 365), (181, 365), (127, 365), (74, 365), (20, 365),
    (20, 25), (74, 25), (127, 25), (181, 25), (234, 25), (288, 25),
    (351, 25), (405, 25), (458, 25), (512, 25), (565, 25), (619, 25)
]

def draw_board_gui():
    root = tk.Tk()
    root.title("Backgammon GUI")
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    # Load and draw background board
    board_img = Image.open(BOARD_IMAGE_PATH)
    board_photo = ImageTk.PhotoImage(board_img)
    canvas.create_image(0, 0, anchor=tk.NW, image=board_photo)

    # Placeholder: Draw circle tokens on the board based on POINT_POSITIONS
    for i, (x, y) in enumerate(POINT_POSITIONS):
        canvas.create_oval(x, y, x + 20, y + 20, outline='gray', fill='', width=1)

    root.mainloop()

if __name__ == "__main__":
    draw_board_gui()
