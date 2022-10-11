class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # brute force TLE
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if sum(nums[i:j+1]) == goal:
        #             count+=1
        # return count
        '''Implementing Sliding window solution'''
        def helper(nums,goal):
            if goal<0: return 0 # its not possible becouse bin no
            res = cur_sum = 0
            start = 0
            n = len(nums)
            for end in range(n):
                cur_sum+=nums[end]
                while cur_sum > goal:
                    cur_sum-=nums[start]
                    start+=1
                res += (end-start+1)
            return res
        return helper(nums,goal)-helper(nums,goal-1)
        
        
        
        
        
        '''
        We can use prefix map and here intution is sm[i,j] = sm[0,j]-sm[0,i]
        Since we are only want to delete subarray which is prev or that to get sum==k
        So we cann't precompute prefix
        we have do it at the same time while we are computing sm and prefixsum in one         loop
        We have to handle edge case where sum of [] prefix subarray is 0. when prefix         sum is exactly == goal 
        O(n) - time and space
        '''
        # sm = 0
        # res = 0
        # pre_sm_count = {0:1}
        # for num in nums:
        #     sm+=num
        #     if sm-goal in pre_sm_count:
        #         res+=pre_sm_count[sm-goal]
        #     pre_sm_count[sm] = pre_sm_count.get(sm,0)+1
        # return res