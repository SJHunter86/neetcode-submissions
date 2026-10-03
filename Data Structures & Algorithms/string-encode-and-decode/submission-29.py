class Solution:

    def encode(self, strs: List[str]) -> str:
        # need length and delimeter
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += f"{length}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        # "3#cat5#water4#cars"
        # get the length
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j].isdigit():
                j += 1
            length = int(s[i:j])
            # j is now on the delimeter
            word = s[j+1:j+1+length]
            result.append(word)
            i = j + 1 + length
        return result