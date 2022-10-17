class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        o_prefix = {0:1}
        count = 0
        res = 0
        for n in nums:
            if n%2!=0:
                count+=1
                o_prefix[count] = 1
            else:
                o_prefix[count]+=1
            if count-k in o_prefix:
                res+= o_prefix[count-k]
                
        return res