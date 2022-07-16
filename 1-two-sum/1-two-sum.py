class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index,elem in enumerate(nums):
            search = target - elem
            if search in hmap:
                return (hmap[search],index)
                # return (min(index,hmap[search]),max(index,hmap[search]))
            else:
                hmap[elem] = index
        