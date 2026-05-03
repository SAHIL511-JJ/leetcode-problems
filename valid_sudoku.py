"""
LeetCode #36: Valid Sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.
"""


def is_valid_sudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue

            if val in rows[r]:
                return False
            rows[r].add(val)

            if val in cols[c]:
                return False
            cols[c].add(val)

            box_idx = (r // 3) * 3 + (c // 3)
            if val in boxes[box_idx]:
                return False
            boxes[box_idx].add(val)

    return True


if __name__ == "__main__":
    test_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(f"Valid Sudoku: {is_valid_sudoku(test_board)}")
