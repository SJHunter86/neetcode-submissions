class Solution:

    def encode(self, strs: List[str]) -> str:
        # build a string with a delimiter & length
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            window = j + 1 + length
            word = s[j + 1:window]
            result.append(word)
            i = window
        return result