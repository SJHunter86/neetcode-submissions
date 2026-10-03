class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            c_map = [0] * 26
            for c in s:
                c_map[ord('a')-ord(c)] += 1
            anagrams[tuple(c_map)].append(s)
        
        return [v for v in anagrams.values()]