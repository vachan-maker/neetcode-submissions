class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        for char in s:
            if char == '(':
                stack.append(char)
                top+=1
            elif char == '[':
                stack.append(char)
                top += 1
            elif char == '{':
                stack.append(char)
                top += 1
            elif char == ')' and stack and stack[top] == '(':
                stack.pop()
                top -= 1
            elif char == '}' and stack and stack[top] == '{': 
                stack.pop()
                top -= 1
            elif char == ']' and stack and stack[top] == '[':
                stack.pop()
                top -= 1
            else:
                return False
        return len(stack) == 0
        