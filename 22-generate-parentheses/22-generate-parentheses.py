class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n,"(",result,1,0)
        return result
        
    def dfs(self,n,pair,result,op,c):
        if op==c==n:
            result.append(pair)
            return
        if op <n: self.dfs(n,pair+"(",result,op+1,c)
        if c < op: self.dfs(n,pair+")",result,op,c+1)
        