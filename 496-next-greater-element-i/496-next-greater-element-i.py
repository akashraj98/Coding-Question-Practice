class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm  = {}
        res = []
        for i,el in enumerate(nums2):
            hm[el]=i
        for j in nums1:
            index =hm[j]
            index+=1
            found = 0
            while index< len(nums2):
                if nums2[index]> j:
                    res.append(nums2[index])
                    found = 1
                    break
                index+=1
                
            if not found :res.append(-1)
        return res
    
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # TC: O(m+n) SC: O(m)
#         res = [-1]*len(nums1)
#         nums1indx = {n:i for i,n in enumerate(nums1)}
#         stack = []
        
#         for elem in nums2:           
#             while stack and elem > stack[-1]:
#                 index =nums1indx[stack.pop()]
#                 res[index] = elem
#             if elem in nums1indx:
#                 stack.append(elem)
            
#         return res
        
        
        
        
        
        
        
        
        
        # Approach 2 O(m*n)
        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1indx:
        #         continue
        #     for j in range(i,len(nums2)):
        #         if nums2[j]> nums2[i]:
        #             indx = nums1indx[nums2[i]]
        #             res[indx] = nums2[j]
        #             break
        # return res
                    
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