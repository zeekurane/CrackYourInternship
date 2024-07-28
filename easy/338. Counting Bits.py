class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]+[1 for _ in range(n)]
        if n<2:
            return ans
        else:
            iterator=2
            i=2
            while i<=n:
                j=0
                while i<=n and i<2**iterator:
                    ans[i]+=ans[j]
                    i+=1
                    j+=1
                iterator+=1
            return ans