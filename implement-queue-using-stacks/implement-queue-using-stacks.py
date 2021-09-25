class MyQueue(object):

    def __init__(self):
        self.arr = []
        
    
    def push(self, x):
        """
        Pushes element x to the back of the queue
        """
        self.arr.append(x)
        

    def pop(self):
        """
        Removes the element from the front of the queue and returns it
        """
        if not self.empty():
            return self.arr.pop(0)
        

    def peek(self):
        """
        Returns the element at the front of the queue
        """
        if not self.empty():
            return self.arr[0]
        

    def empty(self):
        """
         Returns true if the queue is empty, false otherwise
        """
        return False if self.arr else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()