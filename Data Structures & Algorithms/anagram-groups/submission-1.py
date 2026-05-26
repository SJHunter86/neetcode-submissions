class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort the string and set it as a key for the map, add string to value array
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return [value for key, value in groups.items()]