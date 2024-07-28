class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        ones=0
        
        def exchange(l,r):
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
        
        while ones<=right:
            if nums[ones]==0:
                exchange(left,ones)
                left+=1
            elif nums[ones]==2:
                exchange(right,ones)
                right-=1
                ones-=1
            ones+=1