class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left,right,nums):
            nl = len(left)
            nr = len(right)
            res = []
            count=0
            i=0
            j=0
            for i in range(len(left)):
                while j<len(right) and left[i]>right[j]*2:
                    j+=1
                count+=j
            i=0
            j=0
            while i<nl and j<nr:
                if left[i]>right[j]:
                    res.append(right[j])
                    j+=1
                else:
                    res.append(left[i])
                    i+=1
            res+=left[i:]         
            res+=right[j:]
            return res,count


        def mergeSort(nums):
            if len(nums)<2:
                return nums,0
            mid = len(nums)//2
            Left,count1 = mergeSort(nums[:mid])
            Right,count2 = mergeSort(nums[mid:])
            arr,count3 = merge(Left,Right,nums)
            return arr,(count1+count2+count3)
        arr,count = mergeSort(nums)
        return count
        
        
            
        