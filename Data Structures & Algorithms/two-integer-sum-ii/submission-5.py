class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        result = []

        left = 0
        right = len(numbers) - 1
    
        while left < right:
            if numbers[left] + numbers[right] == target:
                result.append(left + 1)
                result.append(right + 1)
                break
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
        return result

                
            
