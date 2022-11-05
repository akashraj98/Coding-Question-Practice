class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for num in nums:
            if count.get(num,0)>1:
                continue
            prev=count.get(num-1,0)
            nxt = count.get(num+1,0)

            if not prev and not nxt:
                res.append(num)
        return res