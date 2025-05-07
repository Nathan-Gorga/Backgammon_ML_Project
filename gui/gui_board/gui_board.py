import os
import tkinter as tk
from PIL import Image, ImageTk

script_dir = os.path.dirname(os.path.abspath(__file__))

BOARD_IMAGE_PATH = os.path.join(script_dir, './board_assets/board.png')
BLACK_TOKEN_PATH = os.path.join(script_dir, '../gui_token/token_assets/black_token.png')
WHITE_TOKEN_PATH = os.path.join(script_dir, '../gui_token/token_assets/white_token.png')

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 400

POINT_POSITIONS = [
    (614, 365), (560, 365), (507, 365), (453, 365), (400, 365), (346, 365),
    (283, 365), (229, 365), (176, 365), (122, 365), (69, 365), (15, 365),
    (15, 10), (69, 10), (122, 10), (176, 10), (229, 10), (283, 10),
    (346, 10), (400, 10), (453, 10), (507, 10), (560, 10), (614, 10)
]

TOKEN_START_POSITION = [
    (0, 'white'), (0, 'white'),
    (5, 'black'), (5, 'black'), (5, 'black'), (5, 'black'), (5, 'black'), 
    (7, 'black'), (7, 'black'), (7, 'black'),
    (11, 'white'), (11, 'white'), (11, 'white'), (11, 'white'), (11, 'white'),

    (12, 'black'), (12, 'black'), (12, 'black'), (12, 'black'), (12, 'black'),
    (16, 'white'), (16, 'white'), (16, 'white'),
    (18, 'white'), (18, 'white'), (18, 'white'), (18, 'white'), (18, 'white'),
    (23, 'black'), (23, 'black')
]

def draw_board_gui():
    root = tk.Tk()
    root.title("Backgammon GUI")
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    board_img = Image.open(BOARD_IMAGE_PATH)
    board_photo = ImageTk.PhotoImage(board_img)

    black_token_img = ImageTk.PhotoImage(Image.open(BLACK_TOKEN_PATH).resize((30, 30)))
    white_token_img = ImageTk.PhotoImage(Image.open(WHITE_TOKEN_PATH).resize((30, 30)))

    canvas.board_photo = board_photo
    canvas.black_token_img = black_token_img
    canvas.white_token_img = white_token_img

    canvas.create_image(0, 0, anchor=tk.NW, image=board_photo)

    point_stacks = {}
    for idx, color in TOKEN_START_POSITION:
        point_stacks.setdefault(idx, []).append(color)

    for idx, tokens in point_stacks.items():
        x, y = POINT_POSITIONS[idx]
        is_bottom_half = idx <= 11  # points 0-11

        visible_tokens = tokens[:5]
        extra_count = len(tokens) - 5

        for i, color in enumerate(visible_tokens):
            offset = -i * 12 if is_bottom_half else i * 12  # toward center
            canvas.create_image(x, y + offset, anchor=tk.NW, image=black_token_img if color == 'black' else white_token_img)

        if extra_count > 0:
            final_offset = -5 * 12 if is_bottom_half else 5 * 12
            canvas.create_text(x + 15, y + final_offset + 15, text=f"+{extra_count}", fill="red", font=("Arial", 10, "bold"))

    root.mainloop()

if __name__ == "__main__":
    draw_board_gui()
