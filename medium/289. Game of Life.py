class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dies=set()
        alive=set()
        z=[[-1,-1],[-1,0],[-1,+1],
          [0,-1],[0,+1],
          [+1,-1],[+1,0],[+1,+1]]
        rows=len(board)
        cols=len(board[0])
        for r in range(rows):
            for c in range(cols):
                ones=0
                for cell in z:
                    if 0<=r+cell[0]<rows and 0<=c+cell[1]<cols and board[r+cell[0]][c+cell[1]]==1:
                        ones+=1
                if board[r][c]==1:
                    if (ones<2 or ones>3):
                        dies.add((r,c))
                else:
                    if ones==3:
                        alive.add((r,c))
        for die in dies:
            board[die[0]][die[1]]=0
        for rebirth in alive:
            board[rebirth[0]][rebirth[1]]=1