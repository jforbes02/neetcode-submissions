class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rules = {'[':']', '{':'}', '(':')'}
        
        for ch in s:
            if ch in rules:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if rules[stack.pop()] != ch:
                    return False
        return len(stack) == 0
                
            