class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make the key a sorted tuple of the word - add it as a value to the list - return a list of lists
        anagrams = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())