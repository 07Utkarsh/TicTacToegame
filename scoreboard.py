class Scoreboard():
    def __init__(self):
        self.user_points=0
        self.computer_points=0

    def points(self, player):
        if player == "X":
            self.user_points+=1
        else:
            self.computer_points+=1

    def print_results(self):
        if self.user_points>self.computer_points:
            print("PLAYER POINTS             COMPUTER POINTS")
            print(f"      {self.user_points}                           {self.computer_points}")
            print("Congrats, overall you defeated computer")
        elif self.user_points<self.computer_points:
            print("PLAYER POINTS             COMPUTER POINTS")
            print(f"      {self.user_points}                           {self.computer_points}")
            print("Too bad you were defeated, better luck next time")
        else:
            print("PLAYER POINTS             COMPUTER POINTS")
            print(f"      {self.user_points}                           {self.computer_points}")
            print("Nice try, it's a draw")
