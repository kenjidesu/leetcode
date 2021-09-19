class Solution(object):
    def twoSum(self, numbers, target):
        # generate hashmap
        hashMap = {}
        # enumerate() - returns (ith place, ith element)
        for i, n in enumerate(numbers):
            # result will be the other number algorithm is finding
            diff = target - n
            # checks if diff is in hashMap
            if diff in hashMap:
                # returns ith 1-index of diff, current ith 1-index
                return hashMap[diff] + 1, i + 1
            # appends (ith element, 1-ith index) to the hashMap
            hashMap[n] = i
        