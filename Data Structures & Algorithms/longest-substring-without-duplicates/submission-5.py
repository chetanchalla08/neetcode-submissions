class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        best = 0

        for letter in range(len(s)):
            while s[letter] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[letter])
            best = max(best, letter - left + 1)

        return best
        