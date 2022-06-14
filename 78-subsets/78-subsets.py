class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums,[],result)
        
        return result
        
        
    def dfs(self,nums,subset,result):
        if len(nums)==0:
            result.append(subset)
            return
        self.dfs(nums[1:],subset+[nums[0]],result)
        self.dfs(nums[1:],subset,result)
        
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         self.dfs(nums,[],result)
#         return result
    
    
#     def dfs(self, nums,subset,result):
#         result.append(subset)
#         for i in range(len(nums)):
#             self.dfs(nums[i+1:],subset+[nums[i]],result)
    
        
        #Naive approach
#         res = []  # to store result
#         subset = [] # to store subsets
#         def dfs(i):
#             if i >= len(nums):      # base case/exit case
#                 res.append(subset.copy())   # using copy since subset is modified
#                 return
#             # we either include the element at i or not
#             # this can be visualised as binary tree
#             #for left subtree
#             subset.append(nums[i])
#             dfs(i+1)
#             # for right subtree
#             subset.pop()   
#             dfs(i+1)
        
        
#         dfs(0)  # staring dfs with index 0
#         return res 

# # iterative approach cascading
# result = [[]]
#         for n in nums:
#             for i in range(len(result)):
#                 result.append(result[i]+[n])
#         return result