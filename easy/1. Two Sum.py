class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in d:
                return [d[c],i]
            else:
                d[nums[i]]=i
        return []