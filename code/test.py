from sudoku import Board


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


if __name__ == "__main__":
    test_small()

    test_invalid()
