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