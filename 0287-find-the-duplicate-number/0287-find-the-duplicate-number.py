class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def swap(i,j):
            nums[i],nums[j]=nums[j],nums[i]
        ptr =0
        i=0
        while i<len(nums):
            val = nums[i]
            pos = val-1
            if nums[pos] == val and pos !=i:
                return val
            elif nums[pos] == val:
                i+=1
            else:
                swap(i,pos)
                
        