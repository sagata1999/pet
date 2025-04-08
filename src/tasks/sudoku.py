from pprint import pprint


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

def validate_sudoku(board_: list[list[str]]) -> bool:
    valid = False
    print(f"len board: {len(board_)}")
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            section = [[board_[row][col] for col in range(i, i + 3)] for row in range(j, j + 3)]
            section = [k for s in section for k in s]
            pprint(section)



validate_sudoku(board)
