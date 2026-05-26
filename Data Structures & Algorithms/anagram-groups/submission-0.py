class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map; keys are sorted strings, value is an array
        anagrams = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            anagrams[key].append(str)
        return [val for key, val in anagrams.items()]