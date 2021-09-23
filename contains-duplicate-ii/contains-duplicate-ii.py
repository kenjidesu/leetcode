class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # generate hashmap
        hsh = {}
        for i in range(len(nums)):
            # check if its in hashmap
            if nums[i] in hsh:
                # if <= k, true
                if i - hsh.get(nums[i]) <= k:
                    return True
            # append val, index
            hsh[nums[i]] = i
        return False