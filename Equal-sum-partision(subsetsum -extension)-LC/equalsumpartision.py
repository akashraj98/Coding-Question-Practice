class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if (total%2) != 0:
            return False
        else:
            return self.isSubsettotal(len(nums),nums,total//2)

    def isSubsettotal(self, N, arr, total):
        memo = [[False]*(total+1) for _ in range(N+1)]
        
        for i in range(N+1):
            memo[i][0]=True
        
        for i in range(1,N+1):
            for j in range(1,total+1):
                if arr[i-1]<= j:
                    memo[i][j] = memo[i-1][j] or memo[i-1][j-arr[i-1]] 
                else:
                    memo[i][j] = memo[i-1][j] 
        
        return memo[N][total]
        