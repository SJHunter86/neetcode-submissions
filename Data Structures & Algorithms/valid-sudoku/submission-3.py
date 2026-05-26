class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # loop through the board adding cells to sets false if its already in the set
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell != ".":
                    if cell in rows[r] or cell in cols[c] or cell in grid[(r // 3, c // 3)]:
                        return False
                    rows[r].add(cell)
                    cols[c].add(cell)
                    grid[(r//3, c//3)].add(cell)
        
        return True