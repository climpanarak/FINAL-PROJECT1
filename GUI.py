import tkinter as tk
from game import RockPaperScissors

class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.game = RockPaperScissors()

        # Set up the widgets
        self.user_choice_label = tk.Label(self, text="Your choice:")
        self.user_choice_label.pack()

        self.user_choice_var = tk.StringVar(self)
        self.user_choice_var.set("rock")
        self.user_choice_option_menu = tk.OptionMenu(self, self.user_choice_var, "rock", "paper", "scissors")
        self.user_choice_option_menu.pack()

        self.computer_choice_label = tk.Label(self, text="Computer's choice: ")
        self.computer_choice_label.pack()

        self.result_label = tk.Label(self, text="Result: ")
        self.result_label.pack()

        self.play_button = tk.Button(self, text="Play", command=self.play_game)
        self.play_button.pack()

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_game)
        self.reset_button.pack()

        self.pack()

    def play_game(self):
        user_choice = self.user_choice_var.get()
        result = self.game.play(user_choice)
        self.computer_choice_label.config(text=f"Computer's choice: {self.game.computer_choice}")
        self.result_label.config(text=f"Result: {result}")

    def reset_game(self):
        self.game.reset_points()
        self.computer_choice_label.config(text="Computer's choice: ")
        self.result_label.config(text="Result: ")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")  # Set the size of the window
    root.title("RockPaperScissors")
    game = Game(master=root)
    game.mainloop()
