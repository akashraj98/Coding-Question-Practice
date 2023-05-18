#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meeting =zip(start,end)
        meeting = sorted(meeting,key = lambda x:x[-1])
        # print(meeting)

        pt1 = ptr2 = 0
        count = 1
        while pt1 < n:
            if meeting[pt1][0]>meeting[ptr2][1]:
                count+=1
                ptr2 = pt1
            pt1+=1
        return count
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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends