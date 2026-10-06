class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1)
        target = Counter(s1)

        while right <= len(s2):
            window = s2[left:right]
            window_count = Counter(window)
            if window_count == target:
                return True
            left += 1
            right += 1
        
        return False




"""
- Sliding window across s2, checking for candidacy
- it has to be a window of len(s)

lecabee
  | |
"""