class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    pass
                elif i==0:
                    grid[i][j]+=grid[i][j-1]
                elif j==0:
                    grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]
        
        
        
        # dp = [[-1]*(n) for _ in range(m)]
        # def countainPath(i,j,m,n,sm):
        #     if i == (m-1) and j == (n-1):
        #         return sm
        #     if i>=m or j>=n:
        #         return 999
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     else:
        #         sm1 =sm2 =sm
        #         if not i+1>= m:
        #             sm1 = sm+grid[i+1][j]
        #         if not j+1 >= n:
        #             sm2 = sm+grid[i][j+1]
        #         first = countainPath(i+1,j,m,n,sm1)
        #         second = countainPath(i,j+1,m,n,sm2)
        #         dp[i][j] = min(first,second)
        #         return dp[i][j]
        # return countainPath(0,0,m,n,grid[0][0])
     