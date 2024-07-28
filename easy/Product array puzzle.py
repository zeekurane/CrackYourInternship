class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        pre_mul=[1 for _ in range(n+1)]
        post_mul=[1 for _ in range(n+1)]
        p=[1 for _ in range(n)]
        
        num=1
        for i in range(n):
            num*=nums[i]
            pre_mul[i+1]=num
        
        num=1
        for i in range(n):
            num*=nums[-i-1]
            post_mul[i+1]=num
        
        for i in range(n):
            p[i]=pre_mul[i]*post_mul[-i-2]
        
        return p