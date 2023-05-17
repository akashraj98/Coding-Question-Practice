class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1s = 0
        curr_1s = 0
        for i in range(len(nums)):
            if nums[i]==1:
                curr_1s+=1
                max_1s = max(max_1s,curr_1s)
            else:
                curr_1s = 0

        return max_1s