from sudoku import Board, backtrack


def small() -> Board:
    b = Board(n=2)
    b.board = [
                [1, 0, 0, 0],
                [2, 0, 4, 1],
                [3, 0, 0, 0],
                [4, 0, 0, 0],
              ]

    return b


def invalid() -> Board:
    b = Board(n=2)
    b.board = [
                [1, 0, 0, 0],
                [1, 0, 4, 1],
                [3, 0, 0, 0],
                [4, 0, 0, 0],
              ]
    return b


def superhard() -> Board:
    """Sudoku from https://www.websudoku.com/?level=4&set_id=9244429135""" 
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
    return b


def test_board(name: str, board: Board):
    print(f"=== Sudoku: {name} ===")
    print(board)

    exists, solution = backtrack(board)

    if exists:
        print("Solution exists!")
        print(solution)
    else:
        print("Solution does not exist!")

    print("\n\n")


if __name__ == "__main__":
    test_board("Small", small())
    test_board("Invalid", invalid())
    test_board("Superhard", superhard())

