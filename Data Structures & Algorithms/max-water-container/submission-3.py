class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0

        while left < right:
            width = right - left
            water_height = min(heights[right], heights[left]) 

            area = width * water_height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
            best = max(area, best)
        
        return best