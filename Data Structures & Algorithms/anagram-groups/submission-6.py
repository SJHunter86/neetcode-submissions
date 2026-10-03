class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            k = self.tupleKey(s)
            anagrams[k].append(s)
        
        return list(anagrams.values())
        
    def tupleKey(self, candidate: str) -> tuple[int, ...]:
        encoded = [0] * 26
        for c in candidate:
            encoded[ord(c) - ord('a')] += 1
        return tuple(encoded)