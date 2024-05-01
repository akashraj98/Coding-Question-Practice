
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        if n==0 or W==0:
            return 0
        if wt[n-1]<=W:
            return max(val[n-1]+self.knapSack(W-wt[n-1],wt,val,n-1)
                ,self.knapSack(W,wt,val,n-1))
        else:
            return self.knapSack(W,wt,val,n-1)
       
