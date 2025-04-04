'''
3. Implement the Guess-my-Number game in the OOP framework

    Computer has chose a number (1, 100), can you guess? Max. 10 guesses

    -> 35
    Higher

    -> 65
    Lower

    -> 44
    Higher

    -> 45
    Correct!!

    Number of attempts 4/10
    Excellent playing!'''

import random

class GuessMyNumber:
    def __init__(self):

        self.number = random.randint(1, 100)
        self.max = 10
        self.attempts = 0
        self.game_over = False

    def guess(self, user_guess):
        if self.game_over:
            print("The game is over")
            return
        
        self.attempts += 1
        
        if user_guess < self.number:
            print("A bit Higher")
        elif user_guess > self.number:
            print("A bit Lower")
        else:
            print("Correct!!")
            print(f"Number of attempts: {self.attempts}/{self.max}")
            if self.attempts <= 5:
                print("Excellent playing!")
            else:
                print("Good job!")
            self.game_over = True

        if self.attempts >= self.max and not self.game_over:
            print(f"Game Over! The number was {self.number}.")
            self.game_over = True

    
if __name__ == "__main__":
    game = GuessMyNumber()
    
    while not game.game_over:
        user_input = input(f"Attempt {game.attempts + 1}/{game.max} - Guess the number: ")
        try:
            user_guess = int(user_input)
            if 1 <= user_guess <= 100:
                game.guess(user_guess)
            else:
                print("Please guess a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter an integer.")


