class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0] * 26

        for i in range(len(s)):
            sc = ord(s[i]) - ord('a')
            tc = ord(t[i]) - ord('a')
            chars[sc] += 1
            chars[tc] -= 1
        
        for num in chars:
            if num != 0:
                return False
        
        return True
        