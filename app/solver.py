class SudokuSolver():
    def __init__(self, board) -> None:
        self.board = board

    def find_empty_space(self) -> tuple | None:
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
                
        return None
    
    def solve(self) -> bool:
        empty_space = self.find_empty_space()
        if empty_space == None:
            return True # puzzle is solved
        else:
            row, column = empty_space
            for i in range(1, 10):
                if self.validate_move(i, row, column) is True:
                    self.board[row][column] = i

                    if self.solve():
                        return True
                    
                    self.board[row][column] = 0

            return False # couldnt find solution

    def validate_move(self, num: int, row: int, column: int) -> bool:
        if num in self.board[row]:
            return False
        
        for i in range(9):
            if self.board[i][column] == num:
                return False
            
        start_row, start_column = 3 * (row // 3), 3 * (column // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_column, start_column + 3):
                if self.board[i][j] == num:
                    return False
                
        return True
    
    def visualise_board(self):
        board_str = ""
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                board_str += "- - - - - - - - - - - -\n"

            for j in range(len(self.board[i])):
                if j % 3 == 0 and j != 0:
                    board_str += "| "

                if j == 8:
                    board_str += str(self.board[i][j]) + "\n"
                else:
                    board_str += str(self.board[i][j]) + " "

        return board_str
    
    @property
    def solved(self):
        result = self.solve()
        if result is False:
            return "Couldn't find solution"
        else:
            return self.visualise_board()

# testing functionality
""" my_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

solver = SudokuSolver(my_board)
print(solver.solved) """