"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

"""

from typing import List


class Solution:
    def check_sub_grid(self, board: List[List[str]]) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])

        # potrei anche prendere la sotto griglia e fare gli stessi check.

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = set()
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        current = board[row][col]
                        if current == ".":
                            continue
                        if current not in seen:
                            seen.add(current)
                        else:
                            return False

        return True

    def check_columns(self, board: List[List[str]]) -> bool:

        n_cols = len(board[0])
        n_rows = len(board)
        transpose = []

        for col in range(n_cols):
            column = [board[row][col] for row in range(n_rows)]
            transpose.append(column)

        return self.check_rows(transpose)

    def check_rows(self, board: List[List[str]]) -> bool:

        for row in board:
            seen = set()
            for current in row:
                if current == ".":
                    continue
                if current not in seen:
                    seen.add(current)
                else:
                    return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.check_sub_grid(board)
            and self.check_rows(board)
            and self.check_columns(board)
        )
