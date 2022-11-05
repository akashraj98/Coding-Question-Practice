class Solution:
    def findFinalValue(self, nums: List[int], origin: int) -> int:
        nums = sorted(nums)
        while origin in nums:
            origin=origin*2
        return origin