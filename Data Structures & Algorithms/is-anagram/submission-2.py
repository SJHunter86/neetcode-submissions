class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_table = [0] * 26
        for i in range(len(s)):
            s_c = ord(s[i]) - ord('a')
            t_c = ord(t[i]) - ord('a')
            freq_table[s_c] += 1
            freq_table[t_c] -= 1
        
        for num in freq_table:
            if num != 0:
                return False
        
        return True