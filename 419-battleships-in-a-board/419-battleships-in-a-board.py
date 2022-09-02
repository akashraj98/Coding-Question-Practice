class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i>=len(board) or j>= len(board[0]) or board[i][j] !="X":
                return
            board[i][j] = "."
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== "X":
                    dfs(i,j)
                    count+=1
        return count