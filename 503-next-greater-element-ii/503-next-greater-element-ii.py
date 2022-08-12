class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]* n
        stack = []
        for _ in [0,1]:
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    index = stack.pop()
                    res[index] = nums[i]
                stack.append(i)
        return res
