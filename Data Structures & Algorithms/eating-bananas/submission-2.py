class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            speed = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += pile//speed

                if pile%speed != 0:
                    hours += 1
            
            if hours <= h:
                answer = speed
                right = speed - 1
            else:
                left = speed + 1
            
        return answer