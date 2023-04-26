class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 in nums_set:
                continue
            else:
                count = 0
                elem = num
                while elem in nums_set:
                    count+=1
                    elem = elem+1
                max_count = max(max_count,count)
        return max_count