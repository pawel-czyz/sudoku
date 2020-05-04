from sudoku import Board, backtrack


def small_board() -> Board:
    b = Board(n=2)
    
    b.board[0][0] = 1
    b.board[1][0] = 2
    b.board[2][0] = 3
    b.board[3][0] = 4

    b.board[1][2] = 4
    b.board[1][3] = 1

    return b


def test_small():
    print("=== Favourite example: small board ===")
    small = small_board()

    print(small)

    print("0th row")
    print(small.get_row(0))

    print("0th column")
    print(small.get_column(0))


    print("0-0 square")
    print(small.get_square(0, 0))

    print("0-1 square")
    print(small.get_square(0, 1))

    print("Is this valid?")
    print(small.is_valid())
    print("\n\n")

    print("Solving sudoku")
    exists, board = backtrack(small)

    print(exists)
    print(board)

def test_invalid():
    print("=== Another (invalid this time) board ===")
    b = Board(n=2)
    
    b.board[0][0] = 1
    b.board[1][0] = 1
    b.board[2][0] = 3
    b.board[3][0] = 4

    print(b)
    print("Is this valid?")
    print(b.is_valid())


def test_superhard():
    """Sudoku from https://www.websudoku.com/?level=4&set_id=9244429135""" 
    print("=== Super-hard sudoku ===")
    b = Board(n=3)
    b.board = [
            [0, 4, 0, 8, 6, 0, 0, 7, 0],
            [0, 2, 5, 0, 0, 0, 8, 0, 0],
            [0, 0, 0, 0, 0, 5, 0, 0, 4],
            [0, 0, 9, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 5, 0, 4, 3, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [5, 0, 0, 7, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 4, 1, 0],
            [0, 7, 0, 0, 1, 6, 0, 9, 0],
            ]
    _, solution = backtrack(b)
    print(solution)


if __name__ == "__main__":
    test_small()

    test_invalid()

    test_superhard()
