class Board():

    def __init__(self):
        self.board = [" "]*9
        pass

    def reset(self):
        self.board = [" "]*9

    def display(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")
    
    def isFull(self):
        return " " not in self.board
    
    def isValid(self,move):
        return 1 <= move <= 9 and self.board[move-1] == " "
    
    def updateBoard(self, move, symbol):
        if self.isValid(move):
            self.board[move-1] = symbol
            return True
        return False
        