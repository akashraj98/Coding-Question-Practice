class Solution:
    def pivot(self,l,r,nums):
        while l<r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1
        return l
    
    def bsearch(self,l,r,target,nums):
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            if target < nums[mid]:
                r = mid-1
            else:
                l = mid+1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        # find pivot  
        n = len(nums)
        if n == 1 and nums[0] ==target: return 0
        pivot_in = self.pivot(0,len(nums)-1,nums)
        # if l==0:
        #     start = 0
        #     end = n-1
        # else:
        #     start = l
        #     end = l-1
#         if target < nums[start] or target > nums[end]:
#             return -1
#         if target == nums[start]: return start
#         if target == nums[end]: return end
        
        if target < nums[0]:
            # search space
            return self.bsearch(pivot_in,n-1,target,nums)
        else:
            #search space
            if pivot_in == 0:
                return self.bsearch(0,n-1,target,nums)
            else:
                return self.bsearch(0,pivot_in-1,target,nums)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        