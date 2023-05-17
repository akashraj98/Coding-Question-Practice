class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=i=0
        while j<len(nums):
            if j< len(nums)-1 and nums[j]==nums[j+1]:
                j+=1
                continue
            nums[i]=nums[j]
            i+=1
            j+=1
        return i