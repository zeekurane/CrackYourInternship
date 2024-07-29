class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num=2
        i=0
        while num**i!=n:
            if num**i>n:
                return False
            i+=1
        return True