class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                coord = board[row][col]
                if coord != ".":
                    if coord in rows[row] or coord in cols[col] or coord in squares[(row//3, col//3)]:
                        return False
                    cols[col].add(coord)
                    rows[row].add(coord)
                    squares[(row//3, col//3)].add(coord)
        return True