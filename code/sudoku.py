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
        s = ""
        for i in range(self.size):
            for j in range(self.size):
                s = s + str(self.board[i][j]) + "   "
            s = s + "\n\n"
        return s

