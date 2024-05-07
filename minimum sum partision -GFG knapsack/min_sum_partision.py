#User function Template for python3
class Solution:
    
    def possibleSum(self,arr,n,sum):
        memo = [[False]*(sum+1) for _ in range(N+1)]
        
        for i in range(N+1):
            memo[i][0]=True
        
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]<= j:
                    memo[i][j] = memo[i-1][j] or memo[i-1][j-arr[i-1]] 
                else:
                    memo[i][j] = memo[i-1][j]
        res = []
        for j in range(sum+1):
            if memo[n][j]==True:
                res.append(j)
        return res
                
        
	def minDifference(self, arr, n):
	    arr_range = sum(arr)
	    sums_possible = self.possibleSum(arr,n,arr_range)
	    min_a = 9999999999999
	    for sm in sums_possible:
	        min_a = min(min_a,abs(arr_range-(2*sm)))
	        
	    return min_a
		# code here