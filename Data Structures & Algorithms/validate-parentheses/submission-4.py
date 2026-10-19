class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if pairs[bracket] != stack[-1]:
                    return False
                
                stack.remove(pairs[bracket])

        return not stack