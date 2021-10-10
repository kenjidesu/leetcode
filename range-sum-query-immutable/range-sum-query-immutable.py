class NumArray(object):

    def __init__(self, nums):
        # set nums to self.arr
        self.arr = nums
        

    def sumRange(self, left, right):
        # get the sum of arr[left:right+1]
        return sum(self.arr[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)