class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        self.nums=nums
        self.n=len(nums)
        self.changes=0
        self.nums.sort()
        self.mid=self.nums[self.n//2]
        for i in range(self.n):
            if self.nums[i]<self.mid:
                self.changes+=self.mid-self.nums[i]
            else:
                self.changes+=self.nums[i]-self.mid
        return self.changes