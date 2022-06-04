class Solution:
     def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]
        rowset = set()
        posdiag = set()
        negdiag = set()
        

        def backtrack(col):
            if col == n:
                # Add to res
                nboard = ["".join(row) for row in board]
                res.append(nboard)
                return
            for row in range(n):
                if row in rowset or row+col in posdiag or row-col in negdiag:
                    continue
                rowset.add(row)
                posdiag.add(row+col)
                negdiag.add(row-col)
                board[row][col] = "Q"
                backtrack(col+1)
                rowset.remove(row)
                posdiag.remove(row+col)
                negdiag.remove(row-col)
                board[row][col] = "."
            
        backtrack(0)
        return res
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res = []
#         board = [["."]*n for _ in range(n)]
        
#         def isValidPos(row,col):

#             for i in range(n):
#                 if board[i][col] == "Q":
#                     return False
#             # Vertical
#             for j in range(n):
#                 if board[row][j] == "Q":
#                     return False
#             # Diagonals
#             r= row
#             c = col
#             while r>=0 and c >=0:
                
#                 if board[r][c] == "Q":
#                     return False
#                 r-=1
#                 c-=1
                
#             r= row
#             c = col
#             while r<n and c <n:
                
#                 if board[r][c] == "Q":
#                     return False
#                 r+=1
#                 c+=1
                
#             r= row
#             c = col
#             while r >=0 and c< n:
#                 if board[r][c] == "Q":
#                     return False
#                 r-=1
#                 c-=1
            
#             r =row
#             c = col
#             while r <n and c>=0:
                
#                 if board[r][c] == "Q":
#                     return False
#                 r+=1
#                 c-=1
#             return True
#         def backtrack(col):
#             if col == n:
#                 # Add to res
#                 nboard = ["".join(row) for row in board]
#                 res.append(nboard)
#                 return
#             for row in range(n):
#                 if isValidPos(row,col):
#                     board[row][col] = "Q"
#                     backtrack(col+1)
#                     board[row][col] = "."
#         backtrack(0)
#         return res
        