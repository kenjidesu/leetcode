"""
Time & Space: O(n)

We generate a hash map to store the (ith index, ith element)

Why get the difference of target and ith element?
The result of the difference of target and ith element will be the other number the algorithm is finding.
a - t = b, b + a = t
where a = ith element, t = target value, b = other number

Why we store the (ith index, ith element)?
We store the (ith index, ith element) so when the algorithm got the difference of the target value and
ith element, we can find it easily in our hashmap since we stored our ith element in it and get also the
ith index of that element since we only need to return the indices of the two numbers.
"""
class Solution(object):
    def twoSum(self, nums, target):
        # generate hashmap
        hashMap = {}
        # enumerate() - returns (ith place, ith element)
        for i, n in enumerate(nums):
            # result will be the other number algorithm is finding
            diff = target - n
            # checks if diff is in hashMap
            if diff in hashMap:
                # returns ith index of diff, current ith index
                return hashMap[diff], i
            # appends (ith element, ith index) to the hashMap
            hashMap[n] = i
