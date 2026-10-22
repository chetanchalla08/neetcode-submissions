class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False
        
        target = [0] * 26
        window = [0] * 26

        for char in s1:
            target[ord(char) - ord("a")] += 1

        for right, char in enumerate(s2):
            window[ord(char) - ord("a")] += 1

            if right >= k:
                left_char = s2[right - k]
                window[ord(left_char) - ord("a")] -= 1

            if right >= k-1 and window == target:
                return True

        return False
                
                
            
