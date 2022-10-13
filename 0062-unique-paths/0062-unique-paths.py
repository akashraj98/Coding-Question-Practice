class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        dp = [[-1]*(n) for i in range(m)]
        def countPath(i,j,m,n):
            if i == (m-1) and j == (n-1): return 1
            if i >=m or j>=n: return 0
            if dp[i][j] != -1: return dp[i][j]
            else:
                dp[i][j] = countPath(i+1,j,m,n) + countPath(i,j+1,m,n)
                return dp[i][j]
        
        return countPath(0,0,m,n)