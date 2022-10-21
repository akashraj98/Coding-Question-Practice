class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}
        for i,val in enumerate(nums):
            if val in count and i-count[val] <= k :
                return True
            else:
                count[val]=i
        return False
    
    