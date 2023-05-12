import random

class RockPaperScissors:
    def __init__(self):
        self.computer_choice = ""
        self.user_points = 0
        self.computer_points = 0
        self.result_message = ""

    def play(self, user_choice):
        self.computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == self.computer_choice:
            result = "It's a tie!"
        elif user_choice == "rock" and self.computer_choice == "scissors" \
                or user_choice == "paper" and self.computer_choice == "rock" \
                or user_choice == "scissors" and self.computer_choice == "paper":
            result = "You win!"
            self.user_points += 1
        else:
            result = "Computer wins!"
            self.computer_points += 1

        if self.user_points == 5 or self.computer_points == 5:
            result += " Game over!"

        self.result_message = result  # Store the result message

        return result, self.user_points, self.computer_points

    def reset_points(self):
        self.user_points = 0
        self.computer_points = 0
        self.result_message = ""  # Reset the result message
