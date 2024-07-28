class Solution:
    def exist(self, board, word: str) -> bool:
        
        m=len(board)
        n=len(board[0])
        k=0
        seen=set()
        def dfs(row,col,k):
            if k==len(word):
                return True
            if row<0 or row>=m or col<0 or col>=n or board[row][col]!=word[k] or (row,col) in seen:
                return False
            seen.add((row,col))
            if dfs(row-1,col,k+1) or dfs(row+1,col,k+1) or dfs(row,col-1,k+1) or dfs(row,col+1,k+1):
                return True
            seen.remove((row,col))
            return False
        
        for i in range(m*n):
            if dfs(i//n,i%n,k):
                return True
        return False