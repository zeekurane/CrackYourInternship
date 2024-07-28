class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #1st step flip matrix from middle horixontal
        #2nd step flip matrix from diagonal (upper left - lower right)
        n=len(matrix)
        for i in range(n//2):
            temp=matrix[i]
            matrix[i]=matrix[n-1-i]
            matrix[n-1-i]=temp
        for i in range(n):
            for j in range(n):
                if j>i:
                    temp=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp