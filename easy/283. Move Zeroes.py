class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos=0
        change_pos=0
        while change_pos<len(nums):
            while zero_pos<len(nums) and nums[zero_pos]!=0:
                zero_pos+=1
            change_pos=zero_pos
            while change_pos<len(nums) and nums[change_pos]==0:
                change_pos+=1
            #exchange
            if change_pos>=len(nums) or zero_pos>=len(nums):
                break
            else:
                temp=nums[zero_pos]
                nums[zero_pos]=nums[change_pos]
                nums[change_pos]=temp