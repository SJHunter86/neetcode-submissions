class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # solve for each row, column, grid coord
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for row in range(9):
            for col in range(9):
                coord = board[row][col]
                if coord != ".":
                    if coord in rows[row] or coord in cols[col] or coord in grids[(row//3, col//3)]:
                        return False
                    rows[row].add(coord)
                    cols[col].add(coord)
                    grids[(row//3, col//3)].add(coord)
        return True