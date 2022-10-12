class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i,j = [0,n-1]
        while i in range(0,m)  and j in range(0,n):
            # ex = edge[0]
            # ey = edge[1]
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i+=1
            else:
                return True
        return False
            
        
        
        
        #Approach binary Search
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         #Approach 1
#         for row in matrix:
#             if self.binarySearch(row,target):
#                 return True
#         return False
               
    
#     def binarySearch(self,arr,target):
#         L=0
#         R = len(arr)-1
#         while L<=R:
#             m = (L+R)//2
#             if arr[m]< target:
#                 L= m+1
#             elif arr[m]> target:
#                 R= m-1
#             else:
#                 return True
#         return False
                