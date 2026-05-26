class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting - sorting will normalize it, use as the key
        # value of map is a list, add the unsorted version to list
        # return a lsit of the values of the map (a list[list[str]])
        anagrams = defaultdict(list)

        for word in strs:
            k = "".join(sorted(word))
            anagrams[k].append(word)
        
        return list(anagrams.values())