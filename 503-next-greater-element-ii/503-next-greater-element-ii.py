class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums+nums
        res = []
        for i in range(n):
            found = 0
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    found=1
                    res.append(nums[j])
                    break
            if not found: res.append(-1)
        return res

        