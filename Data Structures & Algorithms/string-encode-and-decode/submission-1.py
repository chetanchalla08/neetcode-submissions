class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))+"#"+word

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            start = j + 1
            length = int(s[i:j])
            word = s[start: start+length]

            result.append(word)

            i = start + length
        return result