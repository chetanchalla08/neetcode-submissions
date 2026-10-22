class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in counts:
                counts[key] = []

            counts[key].append(word)

        return list(counts.values())