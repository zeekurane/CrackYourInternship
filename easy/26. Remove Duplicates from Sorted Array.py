class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        for i in nums:
            if i!=nums[k]:
                k+=1
                nums[k]=i
        return k+1