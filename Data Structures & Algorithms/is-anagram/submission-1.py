class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_table = [0] * 26
        for i in range(len(s)):
            freq_table[ord(s[i]) - ord('a')] += 1
            freq_table[ord(t[i]) - ord('a')] -= 1
        for num in freq_table:
            if num != 0:
                return False
        return True