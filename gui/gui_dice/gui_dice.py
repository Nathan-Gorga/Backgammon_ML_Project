import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))


import tkinter as tk
from PIL import Image, ImageTk


from game.dice.dice import dice, isDouble



class DiceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Backgammon Dice Roller")

        # Load dice images
        script_dir = os.path.dirname(os.path.abspath(__file__))
        assets_path = os.path.join(script_dir, 'dice_assets')
        self.dice_images = [ImageTk.PhotoImage(
            Image.open(os.path.join(assets_path, f"dice{i}.png")).resize((100, 100))
        ) for i in range(1, 7)]


        # Dice image labels
        self.dice1_label = tk.Label(root)
        self.dice1_label.pack(side=tk.LEFT, padx=20, pady=20)

        self.dice2_label = tk.Label(root)
        self.dice2_label.pack(side=tk.LEFT, padx=20, pady=20)

        # Roll button
        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice, font=("Helvetica", 14))
        self.roll_button.pack(pady=10)

        # Double info
        self.double_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.double_label.pack(pady=10)

        # Initial dice
        self.roll_dice()

    def roll_dice(self):
        roll1 = dice()
        roll2 = dice()

        self.dice1_label.config(image=self.dice_images[roll1 - 1])
        self.dice2_label.config(image=self.dice_images[roll2 - 1])
        self.dice1_label.image = self.dice_images[roll1 - 1]
        self.dice2_label.image = self.dice_images[roll2 - 1]

        if isDouble(roll1, roll2):
            self.double_label.config(text="Double! You get four moves.")
        else:
            self.double_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceGUI(root)
    root.mainloop()
