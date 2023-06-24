class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates,subset,target,res):
            if target==0:
                res.append(subset)
                return
            if target <0:
                return 
            
                
            for i in range(len(candidates)):
                if i>0 and candidates[i-1]==candidates[i]:
                    continue
                backtrack(candidates[i+1:],subset+[candidates[i]],target-candidates[i],res)
                
        candidates.sort()
        res =[]
        backtrack(candidates,[],target,res)
        return res
    
        