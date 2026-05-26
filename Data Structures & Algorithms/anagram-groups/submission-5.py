class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            k = "".join(sorted(word))
            anagrams[k].append(word)
        
        return list(anagrams.values())