class MinStack(object):

    def __init__(self):
        self.stack = []
        
    # append to the arr
    def push(self, val):
        self.stack.append(val)
        
    # remove the last element in arr
    def pop(self):
        return self.stack.pop()
        
    # get the first element in arr
    def top(self):
        return self.stack[-1]
        
    # minimum element in arr
    def getMin(self):
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()