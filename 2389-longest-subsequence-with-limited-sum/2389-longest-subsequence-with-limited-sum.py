class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        res = []
        for query in queries:
            cr_sum = 0
            length = 0
            for num in nums:
                if (cr_sum+num <= query):
                    cr_sum+=num
                    length+=1
                else:
                    break
            res.append(length)
        return res
        
        
        """
        sort num
        
        
        
        iterate queries
        {
        int i=0 
        int sz = 0
        sum = 0
        while(i<n)
        {
            if(sum + nums[i] <= queries[j])
                sum += num[i];
                sz++;
            else 
                break;
        }
        
        res.push_back(sz)
        }
        """