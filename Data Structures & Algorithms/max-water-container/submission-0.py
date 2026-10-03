class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        lo, hi = 0, len(heights)-1

        while lo < hi:
            height = min(heights[lo], heights[hi])
            width = hi - lo
            max_area = max(max_area, height * width)
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1
        
        return max_area

"""
measure the max area, increment the smaller of the two sides
"""