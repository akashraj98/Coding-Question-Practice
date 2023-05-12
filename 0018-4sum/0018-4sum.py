class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        r_set = set()
        res = []
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                n_target = target - (nums[i]+nums[j])
                
                l = j+1
                r = n-1
                while l<r:
                    sm=nums[l]+nums[r]
                    if sm < n_target:
                        l+=1
                    elif sm > n_target:
                        r-=1
                    else:
                        quad = (nums[i],nums[j],nums[l],nums[r])
                        if quad in r_set:
                            r-=1
                            continue
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        r_set.add(quad)
                        r-=1
        return res
        