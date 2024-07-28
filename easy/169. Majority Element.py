class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        c=0
        r=0
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        for num, count in d.items():
            if count>c:
                r=num
                c=count
        return r