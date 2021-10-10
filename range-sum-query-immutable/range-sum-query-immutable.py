class NumArray(object):

    def __init__(self, nums):
        self.arr = nums
        

    def sumRange(self, left, right):
        x = sum(self.arr[left:right+1])
        return x
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)