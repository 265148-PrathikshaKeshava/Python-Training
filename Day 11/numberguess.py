import random
 
class G:
    def __init__(self, lb=1, ub=100, ma=10):
        self.lb = lb
        self.ub = ub
        self.ma = ma
        self.s = random.randint(lb, ub)
        self.a = 0
        self.g_over = False
 
    def get_g(self):
        while True:
            try:
                g = int(input(f"Pick a number ({self.lb}-{self.ub}): "))
                if self.lb <= g <= self.ub:
                    return g
                else:
                    print(f"Stay in range ({self.lb}-{self.ub}).")
            except ValueError:
                print("That's not a number!")
 
    def check_g(self, g):
        d = abs(self.s - g)
        if g == self.s:
            print("You got it!")
            return "win"
        elif g < self.s:
            if d <= 3:
                print("So close, a bit higher!")
                return "low-near"
            elif d <= 10:
                print("A bit higher!")
                return "low"
            else:
                print("Way too low!")
                return "lower"
        else:
            if d <= 3:
                print("So close, a bit lower!")
                return "high-near"
            elif d <= 10:
                print("A bit lower!")
                return "high"
            else:
                print("Way too high!")
                return "higher"
 
    def play(self):
        
        print(f"I'm thinking of a number between {self.lb} and {self.ub}. You have {self.ma} tries.")
        while not self.g_over and self.a < self.ma:
            g = self.get_g()
            self.a += 1
 
            result = self.check_g(g)
            if result == "win":
                print(f"Great job! You found it in {self.a}/{self.ma} tries.")
                if self.a <= 4:
                    print("Amazing skills!")
                self.g_over = True
            elif self.a == self.ma:
                print(f"Out of tries! The number was {self.s}. Better luck next time.")
                self.g_over = True
 
if __name__ == "__main__":
    game = G()
    game.play()