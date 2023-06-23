#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    def backtrack(arr,subset,res):
	        res.append(sum(subset))
	        for i in range(len(arr)):
	            backtrack(arr[i+1:],subset+[arr[i]],res)
	    res=[]
	    backtrack(arr,[],res)
	    return res
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends