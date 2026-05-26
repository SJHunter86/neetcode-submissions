class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if their length isnt the same, can't be an anagram
        if len(s) != len(t):
            return False
        
        char_table = [0] * 26
        for i in range(len(s)):
            char_table[ord(s[i]) - ord('a')] += 1
            char_table[ord(t[i]) - ord('a')] -= 1
        
        for num in char_table:
            if num != 0:
                return False

        return True