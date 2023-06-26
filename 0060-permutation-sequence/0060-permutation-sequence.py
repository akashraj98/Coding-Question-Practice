class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def nextPermutation(nums):
            # ind inflextionpt
            # swap hole with biggest number in prev
            # sort remaining 
            hole = 0
            inpt = 0
            md_val = float('inf')
            md_index = 0
            for i in range(len(nums)-1,0,-1):
                if nums[i] > nums[i-1]:
                    hole  = i-1
                    inpt = i
                    break

            for j in range(inpt, len(nums)):
                if nums[j] > nums[hole]:
                    md_val = min(md_val,nums[j]-nums[hole])
                    md_index = j

            nums[hole], nums[md_index] = nums[md_index],nums[hole]
            nums[inpt:] = sorted(nums[inpt:])
            return nums
            
            
        nums = [i+1 for i in range(n)]
        for i in range(k-1):
            nums=nextPermutation(nums)

        res="".join(map(str,nums))
        return res
        