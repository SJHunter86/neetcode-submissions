class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this is a grid of sets, horizontal, vertical, cubes
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        b = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell != ".":
                    row = r[i]
                    col = c[j]
                    box = b[(i // 3)  * 3 + (j//3)]
                    if cell in row or cell in col or cell in box:
                        return False

                    row.add(cell)
                    col.add(cell)
                    box.add(cell)
        return True


"""
i = 0
j = 4
box should be 2

0 // 3 = 0
4 // 3 = 1
"""