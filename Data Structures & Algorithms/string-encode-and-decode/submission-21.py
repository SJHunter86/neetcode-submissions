class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            swapped = s.replace("#", "##")
            result += str(len(swapped)) + "#" + swapped
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            str_len = int(s[i:j])
            coded = s[j+1:j+1+str_len]
            orig = coded.replace("##", "#")
            result.append(orig)
            i = j + 1 + str_len
        return result