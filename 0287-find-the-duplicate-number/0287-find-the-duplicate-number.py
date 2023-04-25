class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        # print(nums2)
        for i in range(1,len(nums2)):
            if nums2[i-1]==nums2[i]:
                return nums2[i]