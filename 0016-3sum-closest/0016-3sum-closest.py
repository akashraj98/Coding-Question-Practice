class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        min_diff= 9999999
        res = nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            start = i+1
            end = n-1
            while start < end:
                sm = nums[i]+nums[start]+nums[end]
                # if sm == target:
                #     return sm
                # if abs(sm - target) < abs(res - target):
                #     res = sm
                diff = abs(sm-target)
                if diff< min_diff:
                    res =sm 
                    min_diff = diff
                if sm< target:
                    start+=1
                elif sm> target: 
                    end-=1
                else:
                    return sm

        return res
            
            