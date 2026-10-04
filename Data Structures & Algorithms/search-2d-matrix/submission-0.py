class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # already sorted
        for row in matrix:
            if row[-1] < target:
                continue
            left, right = 0, len(row)-1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False


# if row[-1] < target, just continue