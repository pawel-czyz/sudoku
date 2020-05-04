from copy import deepcopy


class Board:
    def __init__(self, n: int):
        self.n: int = n
        self.size: int = n * n
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]  # board[i][j] is i-th row, j-th column

    def get_row(self, k: int) -> list:
        pass

    def get_column(self, k: int) -> list:
        pass

    def get_square(self, k: int, l: int) -> list:
        return [self.board[i][j] for i in range(k*self.n, (k+1)*self.n) 
                                 for j in range(l*self.n, (l+1)*self.n)
               ]

    def valid_cell(self, cell: list) -> bool:
        """Returns True if cell is valid, False otherwise."""
        pass

    def is_valid(self) -> bool:
        """Returns True if board is valid, False otherwise."""
        pass

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
        """Returns 'smallest' (i,j) such that entry at (i,j) is 0. 
        If the whole board is filled returns (-1, -1)."""
        pass

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
    pass

