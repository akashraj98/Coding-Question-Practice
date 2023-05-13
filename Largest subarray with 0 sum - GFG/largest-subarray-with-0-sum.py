#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        maxLen = 0
        k = 0
        pSum = 0
        dic = dict()
        for i in range(n):
            pSum+=arr[i]
            if (pSum == k):
                maxLen = i + 1
                
            elif pSum-k in dic:
                length = i- dic[pSum-k]
                maxLen = max(maxLen,length)
            else:
                dic[pSum] = i
                
        return maxLen
        #Code here


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends