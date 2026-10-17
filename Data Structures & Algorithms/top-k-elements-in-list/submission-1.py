class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            
        ordered = sorted(counts.items(), key= lambda pair: pair[1], reverse = True)

        top_pairs = ordered[:k]
        
        result = []

        for pair in top_pairs:
            result.append(pair[0])

        return result