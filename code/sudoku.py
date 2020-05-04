from copy import deepcopy


class Board:
    def __init__(self, n: int):
        self.n: int = n
        self.size: int = n * n
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]  # board[i][j] is i-th row, j-th column

    def get_row(self, k: int) -> list:
        return [self.board[k][i] for i in range(self.size)]

    def get_column(self, k: int) -> list:
        return [self.board[i][k] for i in range(self.size)]

    def get_square(self, k: int, l: int) -> list:
        return [self.board[i][j] for i in range(k*self.n, (k+1)*self.n) 
                                 for j in range(l*self.n, (l+1)*self.n)
               ]

    def valid_cell(self, cell: list) -> bool:
        """Returns True if cell is valid, False otherwise."""
        for item in cell:
            if item != 0 and cell.count(item) > 1:
                return False
        return True

    def is_valid(self) -> bool:
        # Check if all rows are valid
        for i in range(self.size):
            if not self.valid_cell(self.get_row(i)):
                return False

        # Check is all columns are valid
        for i in range(self.size):
            if not self.valid_cell(self.get_column(i)):
                return False

        # Check is all squares are valid
        for i in range(self.n):
            for j in range(self.n):
                if not self.valid_cell(self.get_square(i, j)):
                    return False

        # We've reached this point -- everything must be valid
        return True

    def __str__(self):
        full_string = ""
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                row += str(self.board[i][j])

                if j % self.n == self.n-1 and j != self.size - 1:
                    row += " | "
                else:
                    row += "   "
            
            full_string += row
            if i % self.n == self.n-1 and i != self.size - 1:   
                full_string += "\n" + "-"*(len(row)-3) + "\n"
            else:
                full_string += "\n\n"
        return full_string

    def find_unassigned(self) -> tuple:
        """Returns 'smallest' (i,j) such that entry at (i,j) is 0. If the whole board is filled returns (-1, -1)."""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        # No 0s in the board. Return (-1, -1).
        return (-1, -1)

    def copy(self):
        return deepcopy(self)


def backtrack(board: Board) -> tuple:
    """
    Returns
    -------
    bool
        does a solution exist?
    Board
        solution to the sudoku. The values will be meaningless if the solution does not exist.
    """
    stack = [board]

    while len(stack):

        b: Board = stack.pop()

        i, j = b.find_unassigned()
        
        if i == -1:
            return (True, b)
        
        for digit in range(1, b.size + 1):
            new_b = b.copy()
            new_b.board[i][j] = digit

            if new_b.is_valid():
                stack.append(new_b)

    return (False, board)

