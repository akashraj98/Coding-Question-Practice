class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]== nums[i-1] and i>0:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                val = nums[i]+nums[l]+nums[r]
                if val > 0:
                    r-=1
                elif val<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans