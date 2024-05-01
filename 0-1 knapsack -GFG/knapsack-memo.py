#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def memo_knapSack(self,W, wt, val, n,dp):
        if n==0 or W==0:
            return 0
            
        if dp[W][n]!=-1:
            return dp[W][n]
        else:
            if wt[n-1]<=W:
                dp[W][n] =  max(val[n-1]+self.memo_knapSack(W-wt[n-1],wt,val,n-1,dp)
                    ,self.memo_knapSack(W,wt,val,n-1,dp))
            else:
                dp[W][n] = self.memo_knapSack(W,wt,val,n-1,dp)
            return dp[W][n]
            
    def knapSack(self,W, wt, val, n):
        dp = [[-1]*(n+1) for _ in range(W+1) ]
        res = self.memo_knapSack(W, wt, val, n,dp)
        return res
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends