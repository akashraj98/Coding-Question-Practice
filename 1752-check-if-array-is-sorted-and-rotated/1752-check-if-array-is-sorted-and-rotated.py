class Solution:
    def check(self, nums: List[int]) -> bool:
        inf = 0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                inf+=1
                
        if inf>1:
            return False
        if nums[-1]>nums[0] and inf:
            return False
        return True
                

                
                
            