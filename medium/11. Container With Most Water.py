class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_storage=0
        while left<right:
            water=(right-left)*min(height[left], height[right])
            if water>max_storage:
                max_storage=water
            if height[left]<height[right]:
                left+=1
            elif height[left]>=height[right]:
                right-=1
        return max_storage