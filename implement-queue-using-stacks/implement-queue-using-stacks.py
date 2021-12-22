class MyQueue(object):

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)
        

    def pop(self):
        if not self.empty():
            return self.arr.pop(0)
        

    def peek(self):
        if not self.empty():
            return self.arr[0]
        

    def empty(self):
        return len(self.arr) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()