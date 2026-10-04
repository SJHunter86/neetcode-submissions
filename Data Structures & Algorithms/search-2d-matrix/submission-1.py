class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            mid = (top + bottom) // 2
            row = matrix[mid]
            left, right = 0, len(row)-1
            while left <= right:
                inner_mid = (left + right) // 2
                if row[inner_mid] == target:
                    return True
                elif row[inner_mid] < target:
                    left = inner_mid + 1
                else:
                    right = inner_mid - 1
            if row[-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        
        return False


# if row[-1] < target, just continue