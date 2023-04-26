class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h_map = {}
        for num in nums:
            if num in h_map:
                h_map[num]+=1
            else:
                h_map[num]=1
        for key,val in h_map.items():
            print(val)
            if val> len(nums)/2:
                return key
        