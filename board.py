class Board():
    def print_board(self,list):
        print(f" {list[0][0]} | {list[0][1]} | {list[0][2]}")
        print("------------")
        print(f" {list[1][0]} | {list[1][1]} | {list[1][2]}")
        print("------------")
        print(f" {list[2][0]} | {list[2][1]} | {list[2][2]}")
        print("\n")

    def win_check(self,list,row,col,):
        if (list[row][0] == list[row][1] == list[row][2] == "X") or \
                (list[0][col] == list[1][col] == list[2][col] == "O"):
            return True
        elif (list[0][0] == list[1][1] == list[2][2] == "X") or \
                (list[0][2] == list[1][1] == list[2][0] == "X"):
            return True
        elif (list[0][0] == list[1][1] == list[2][2] == "O") or \
                (list[0][2] == list[1][1] == list[2][0] == "O"):
            return True
        else:
            return False