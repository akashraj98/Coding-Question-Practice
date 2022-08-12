class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]* n
        stack = []
        # for _ in [0,1]:       # constant so it time complexity is O(n)
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                index = stack.pop()
                res[index] = nums[i%n]
            stack.append(i%n)
        return res
