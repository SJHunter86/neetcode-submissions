class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        longest = 1
        left = 0
        for right in range(len(s)):
            # is s[right] in seen?
            if s[right] not in seen:
                longest = max(longest, right - left + 1)
            else: # if its already in there
                while left < right and s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[right])        
        
        return longest
    



"""
{p,w} - set
"pwwkew"
left 0, right 2
longest = 2
n = add right to set, calculate new longest
y = 
p - n
w - n
w - y

"""