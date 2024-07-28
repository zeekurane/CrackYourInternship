class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix) #rows
        n=len(matrix[0]) #columns
        ans=[0 for _ in range(m*n)] #answer, list of spiral elements
        
        #walls
        right=n
        left=-1
        up=-1
        down=m
        
        #controllers
        row_cont=False
        col_cont=True
        row_increase=True
        col_increase=True
        
        #indexes
        row=0
        col=0
        index=0
        
        while up<down-1 and left<right-1:#condition
            if row_cont:
                if row_increase:
                    while row<down:
                        ans[index]=matrix[row][col]
                        index+=1
                        row+=1
                    row-=1
                    col-=1
                    row_increase=not row_increase
                    right-=1
                else:
                    while row>up:
                        ans[index]=matrix[row][col]
                        index+=1
                        row-=1
                    row+=1
                    col+=1
                    row_increase=not row_increase
                    left+=1
            if col_cont:
                if col_increase:
                    while col<right:
                        ans[index]=matrix[row][col]
                        index+=1
                        col+=1
                    col-=1
                    row+=1
                    col_increase=not col_increase
                    up+=1
                else:
                    while col>left:
                        ans[index]=matrix[row][col]
                        index+=1
                        col-=1
                    col+=1
                    row-=1
                    col_increase=not col_increase
                    down-=1
                
            row_cont=not row_cont
            col_cont=not col_cont
        return ans