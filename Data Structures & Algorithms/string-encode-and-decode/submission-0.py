class Solution:
    def encode(self, strs: List[str]) -> str:
        # encode_res = ""
        encode_res = ""
        for s in strs:
            encode_res += str(len(s)) + '#' + s
        return encode_res

    def decode(self, s: str) -> List[str]:
        # "5#hello5#world"
        decode_res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            word = s[j+1: j+1+length]

            decode_res.append(word)

            i = j + 1 + length

        return decode_res

