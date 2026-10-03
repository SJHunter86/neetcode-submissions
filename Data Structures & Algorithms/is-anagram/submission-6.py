class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqs = defaultdict(int)

        for i in range(len(s)):
            freqs[s[i].lower()] += 1
            freqs[t[i].lower()] -= 1
        
        for v in freqs.values():
            if v != 0:
                return False
        
        return True