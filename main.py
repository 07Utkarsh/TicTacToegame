from replit import clear
from art import logo
from board import Board
import random
from scoreboard import Scoreboard
Player1="X"
Player2="O"
rows=3
cols=3

board=Board()
scoreboard=Scoreboard()
def play_game():
    list = [[" " for i in range(cols)] for j in range(rows)]
    left_tiles=9
    print(logo)
    row=int(input("Enter the row in which user wants to put there character: "))
    col=int(input("Enter the col in which user wants to put there character: "))
    list[row][col]=Player1
    left_tiles-=1
    board.print_board(list)
    game_on=True

    while game_on:
        row=random.randint(0,2)
        col=random.randint(0,2)
        if list[row][col]!=" ":
            while list[row][col]!=" ":
                row = random.randint(0, 2)
                col = random.randint(0, 2)
        list[row][col]=Player2
        if board.win_check(list,row,col):
            game_on=False
            print("You lost, better luck next time!!! \n ")
            scoreboard.points(Player2)
            return
        left_tiles-=1
        if left_tiles==0:
            game_on=False
            print("Draw, better luck next time!!!\n")
            return
        board.print_board(list)
        row = int(input("Enter the row in which user wants to put there character: "))
        col = int(input("Enter the col in which user wants to put there character: "))
        if list[row][col] != " ":
            while list[row][col] != " ":
                print("The position is not empty. Try once again ")
                row = int(input("Enter the row in which user wants to put there character: "))
                col = int(input("Enter the col in which user wants to put there character: "))
        list[row][col] = Player1
        left_tiles-=1
        if board.win_check(list,row,col):
            print("Congratulations you won!!! \n")
            scoreboard.points(Player1)
            return
        if left_tiles==0:
            game_on=False
            print("Draw, better luck next time!!! \n")
            return


play_again=input("Do you want to play a game of Tic Tac Toe? Type y or n: ").lower()
while play_again=="y":
    clear()
    play_game()
    play_again=input("Do you want to play more? Type y or n ").lower()
scoreboard.print_results()
print("Thanks for playing with us")