class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            escaped_key = s.replace("#", "##")
            result += str(len(escaped_key)) + "#" + escaped_key
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        # initialize first pointer
        i = 0
        # move pointer through string
        while i < len(s):
            # initialize second pointer
            j = i
            # build the integer length to take out of the string - # is the stopping indicator
            while s[j] != "#":
                j += 1
            
            str_len = int(s[i:j])
            escaped_str = s[j+1:j+1+str_len]
            unpacked = escaped_str.replace("##", "#")
            result.append(unpacked)
            i = j + 1 + str_len
        return result