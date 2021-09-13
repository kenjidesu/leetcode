class Solution(object):
    def isValid(self, s):
        # stack, tracking the brackets
        # opclo, dict of the same type of brackets
        stack, opclo = [], {'}': '{', ']': '[', ')': '('}
        
        for i in s:
            if i in opclo:
                # returns False if the brackets of stack.pop() is not the same type
                # or if stack is empty and it also pop() even tho its not the same type
                if not (stack and stack.pop() == opclo[i]):
                    return False
            else:
                stack.append(i)
        
        # returns True if stack is Empty
        return not stack
        