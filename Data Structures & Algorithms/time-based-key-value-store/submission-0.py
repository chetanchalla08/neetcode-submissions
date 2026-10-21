class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        history = self.store[key]

        left = 0
        right = len(history) - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2

            saved_value = history[mid][0]
            saved_time = history[mid][1]

            if saved_time <= timestamp:
                answer = saved_value
                left = mid + 1
            else:
                right = mid - 1
            
        return answer
        
