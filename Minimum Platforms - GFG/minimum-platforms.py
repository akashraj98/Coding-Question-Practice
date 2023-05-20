#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr = sorted(arr)
        dep = sorted(dep)
        i=1
        j=0
        curr = 1
        max_c = 1
        # while i< n:
        #     if arr[i]>dep[j]:
        #         j+=1
        #     else:
        #         curr+=1
        #     i+=1
        #     max_c = max(curr,max_c)
        for i in range(1,n):
            if arr[i]>dep[j]:
                j+=1
            else:
                curr+=1
            max_c = max(curr,max_c)
        return max_c
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends