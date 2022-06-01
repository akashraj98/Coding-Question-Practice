class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i] +nums[i-1]
        return nums
        # arr = [nums[0]]
        # for i in range(1,len(nums)):
        #     arr.append(arr[-1]+ nums[i])
        # return arr