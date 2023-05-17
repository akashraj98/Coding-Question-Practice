class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1s = 0
        curr_1s = 0
        for i in range(len(nums)):
            if nums[i]==1:
                curr_1s+=1
            if nums[i-1]==0 and i>0 and nums[i]==1:
                curr_1s = 1
            max_1s = max(max_1s,curr_1s)

        return max_1s