class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}

        for letter in s:
            counts_s[letter] = counts_s.get(letter, 0) + 1
        for letter in t:
            counts_t[letter] = counts_t.get(letter, 0) + 1

        if counts_s == counts_t:
            return True

        return False