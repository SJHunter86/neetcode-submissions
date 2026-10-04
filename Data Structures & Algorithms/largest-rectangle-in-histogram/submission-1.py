class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][0] > height:
                old_height, start = stack.pop()
                max_area = max(max_area, old_height * (i-start))
            stack.append((height, start))
        
        return max_area

"""
- stack needed to look back at previous height and idx
- (height, start)
- iterate throgh the heights enumerated
- initialize start to the current index
- while the stack still has entries and the stack's height is > current height
- 
"""