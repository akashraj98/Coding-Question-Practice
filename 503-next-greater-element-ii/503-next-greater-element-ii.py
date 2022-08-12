class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1]* len(nums)
        stack = []
        for i in range(len(nums)) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                res[index] = nums[i]
            stack.append(i)
        return res
