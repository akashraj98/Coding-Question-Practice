class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        nums1indx = {n:i for i,n in enumerate(nums1)}
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1indx:
                continue
            for j in range(i,len(nums2)):
                if nums2[j]> nums2[i]:
                    indx = nums1indx[nums2[i]]
                    res[indx] = nums2[j]
                    break
        return res
                    
#         res =[]
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i]==nums2[j]:
#                     break
#             flag = 0
#             while j < len(nums2)-1:
#                 j+=1            
#                 if nums2[j] > nums1[i]:
#                     res.append(nums2[j])
#                     flag =1
#                     break
#             if j >= len(nums2)-1 and flag ==0:
#                 res.append(-1)
                
#         return res