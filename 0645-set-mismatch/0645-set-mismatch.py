class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        dup = 0
        sm = 0
        size = len(nums)
        for n in nums:
            if n in s:
                dup = n
            else:
                sm+=n
                s.add(n)
        sn = size*(size+1)//2
        mis = sn - sm
        return [dup,mis]
        