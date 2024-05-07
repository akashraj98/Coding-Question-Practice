
class Solution:
    def isSubsetSum (self, N, arr, sum):
        memo = [[-1]*(sum+1) for _ in range(N+1)]
        return self.isSubsetSum_memo(N, arr, sum,memo)
        
        
    def isSubsetSum_memo(self, N, arr, sum, memo):
        if sum==0:
            return True
            
        if N==0:
            return False
            
        if memo[N][sum]!=-1:
            return memo[N][sum]
        if arr[N-1]>sum:
            memo[N][sum] =  self.isSubsetSum_memo(N-1,arr,sum,memo)
        else:
            memo[N][sum] = self.isSubsetSum_memo(N-1,arr,sum,memo) or self.isSubsetSum_memo(N-1,arr,sum-arr[N-1],memo)
        return memo[N][sum]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends