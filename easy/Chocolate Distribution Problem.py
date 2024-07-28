class Solution:

    def findMinDiff(self, A,N,M):
        
        # code here
        A.sort()
        min_diff=10**9
        for i in range(N-M+1):
            if A[i+M-1]-A[i]<min_diff:
                min_diff=A[i+M-1]-A[i]
        return min_diff