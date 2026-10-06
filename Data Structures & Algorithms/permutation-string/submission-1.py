class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        left, right = 0, len(s1)
        window_count = Counter(s2[left:right])

        while right <= len(s2):
            if target == window_count:
                return True
            
            if right == len(s2):
                break
                
            window_count[s2[left]] -= 1
            left += 1
            window_count[s2[right]] += 1
            right += 1
        
        return False




"""
- Sliding window across s2, checking for candidacy
- it has to be a window of len(s)

lecabee
  | |
"""