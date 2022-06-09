class Solution:
    def twoSum(self, s_nums: List[int], target: int) -> List[int]:
        start =0
        end = len(s_nums)-1
        result = []
        while start < end:
            if s_nums[start] + s_nums[end] > target:
                end-=1
            elif s_nums[start] + s_nums[end] < target:
                start+=1
            elif  s_nums[start] + s_nums[end] == target:
                break
        print(s_nums[start],s_nums[end])
        return [start+1,end+1]
                