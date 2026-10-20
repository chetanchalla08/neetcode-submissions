class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for today in range(len(temperatures)):
            while stack and temperatures[today] > temperatures[stack[-1]]:
                previous_day = stack.pop()
                answer[previous_day] = today - previous_day
            
            stack.append(today)
            
        return answer