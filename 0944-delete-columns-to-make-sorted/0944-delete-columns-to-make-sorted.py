class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N=len(strs[0])
        count =0
        for i in range(N):
            for j in range(len(strs)-1):
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    count+=1
                    break
        return count