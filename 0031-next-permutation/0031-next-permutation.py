class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1,0,-1):
            if nums[i-1]< nums[i]:
                inf = i-1
                min_diff = 9999
                for k in range(i,len(nums)):
                    if nums[k]>nums[inf] and nums[k]-nums[inf]< min_diff:
                        nxt = k
                        min_diff = min(min_diff,nums[k]-nums[inf])
                        
                nums[inf],nums[nxt] = nums[nxt],nums[inf]
                print(nums)
                nums[inf+1:] = sorted(nums[inf+1:])
                return nums
        return nums.sort()
                
            
        