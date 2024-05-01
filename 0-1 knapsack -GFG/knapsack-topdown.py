class Solution: 
    def knapSack(self,W, wt, val, n):
        dp = [[0]*(W+1) for _ in range(n+1)]
        for i in range(n+1):
            for w in range(W+1):
                if i==0 or w==0:
                   dp[i][w] = 0
                elif wt[i-1]<=w:
                    dp[i][w] = max( val[i-1]+ dp[i-1][w-wt[i-1]],dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
                
        # code here
        return dp[n][W]