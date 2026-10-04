class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        curr_max = 0

        for i in range(n):
            curr_max = max(height[i], curr_max)
            left_max[i] = curr_max
        
        curr_max = 0
        for i in range(n-1,-1,-1):
            curr_max = max(height[i], curr_max)
            right_max[i] = curr_max
        
        total = 0
        for i in range(n):
            total += min(left_max[i], right_max[i]) - height[i]
        
        return total



"""
prefix diffs?
[0,2,0,3,1,0,1,3,2,1]
[0,2,2,3,3,3,3,3,3,3]

rtl
[0,2,0,3,1,0,1,3,2,1]
[3,3,3,3,3,3,3,3,2,1]


 3,1,1,0,0,0,0,0,1,2
"""