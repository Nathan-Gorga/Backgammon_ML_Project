import tkinter as tk
from game.dice.dice import dice, isDouble

class DiceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Backgammon Dice Roller")

        # Dice display
        self.dice_label = tk.Label(root, text="Roll the dice!", font=("Helvetica", 18))
        self.dice_label.pack(pady=20)

        # Roll button
        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice, font=("Helvetica", 14))
        self.roll_button.pack(pady=10)

        # Double info
        self.double_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.double_label.pack(pady=10)

    def roll_dice(self):
        roll1 = dice()
        roll2 = dice()
        self.dice_label.config(text=f"Dice 1: {roll1} | Dice 2: {roll2}")

        if isDouble(roll1, roll2):
            self.double_label.config(text="Double! You get four moves.")
        else:
            self.double_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceGUI(root)
    root.mainloop()
