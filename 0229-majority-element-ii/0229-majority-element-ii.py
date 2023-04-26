class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h_map = {}
        for num in nums:
            if num in h_map:
                h_map[num]+=1
            else:
                h_map[num]=1
        res = []
        for key,val in h_map.items():
            if val> len(nums)/3:
                res.append(key)
        return res
        
        