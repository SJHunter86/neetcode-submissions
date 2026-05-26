class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # static character map if alphabet, hash map if unicode
        c_list = [0 for _ in range(26)]

        for i in range(len(s)):
            c_list[ord(s[i]) - ord('a')] += 1
            c_list[ord(t[i]) - ord('a')] -= 1

        for num in c_list:
            if num != 0:
                return False
        
        return True