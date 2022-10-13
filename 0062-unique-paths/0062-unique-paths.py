class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        dp = [[-1]*(m) for i in range(n)]
        print(dp)
        def countPath(i,j,m,n):
            if i == (n-1) and j == (m-1): return 1
            if i >=n or j>=m: return 0
            if dp[i][j] != -1: return dp[i][j]
            else:
                dp[i][j] = countPath(i+1,j,m,n) + countPath(i,j+1,m,n)
                return dp[i][j]
        
        return countPath(0,0,m,n)