class Solution:
    def trap(self, height: List[int]) -> int:
        # find left max, then go right to left taking the min
        left_max = []
        max_height = height[0]
        total = 0

        for i in range(len(height)):
            max_height = max(max_height, height[i])
            left_max.append(max_height)
        
        max_height = 0
        for i in range(len(height)-1,-1,-1):
            max_height = max(max_height, height[i])
            total += min(max_height, left_max[i]) - height[i]
        
        return total
            

"""
[0,2,0,3,1,0,1,3,2,1] - height
[0,2,2,3,3,3,3,3,3,3] - left to right
[3,3,3,3,3,3,3,3,2,1] - right to left
[0,0,2,0,2,3,2,0,0,0] - 9
"""