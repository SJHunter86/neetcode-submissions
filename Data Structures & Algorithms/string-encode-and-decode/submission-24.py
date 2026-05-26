class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            swapped = s.replace("#", "##")
            result += str(len(swapped)) + "#" + swapped
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            swapped = s[j+1:j+1+length]
            original = swapped.replace("##", "#")
            result.append(original)
            i = j + 1 + length
        return result