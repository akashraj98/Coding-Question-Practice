class Solution:
    def merge(self,L,R,nums):
        i=j=k=0
        while i< len(L) and j <len(R):
            if L[i]<=R[j]:
                nums[k]= L[i]
                i+=1
            else:
                nums[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            nums[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            nums[k]= R[j]
            j+=1
            k+=1
            
    def mergeSort(self,nums):
        if len(nums)>1:
            mid = len(nums)//2
            L=  nums[:mid]
            R = nums[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            self.merge(L,R,nums)
        return nums
    
    
    def sortArray(self, nums: List[int]) -> List[int]:
        res = self.mergeSort(nums)
        return res