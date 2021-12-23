class Solution(object):
    def isValid(self, s):
        brackets = {')': '(', '}': '{', ']': '['}
        
        valid = []
        for i in s:
            if i in brackets and len(valid) != 0:
                if valid[-1] == brackets[i]:
                    valid.pop()
                else:
                    return False
            else:
                valid.append(i)
                
        return len(valid) == 0