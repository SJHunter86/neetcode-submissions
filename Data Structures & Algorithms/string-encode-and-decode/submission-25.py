class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            modded = s.replace("#", "##")
            leng = len(modded)
            result += str(leng) + "#" + modded
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            encoded = s[j+1:j+1+word_len]
            cleaned = encoded.replace("##", "#")
            result.append(cleaned)
            i = j + 1 + word_len
        return result

