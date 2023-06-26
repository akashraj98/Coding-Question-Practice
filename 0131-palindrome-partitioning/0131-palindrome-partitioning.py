class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrom(subset):
            if subset:
                return subset[::-1]==subset
            return False
        def backtrack(s,subset,res):
            if not s:
                res.append(subset)
                return
            for i in range(len(s)):
                # here instead fo taking one element and putting in subset
                # we need to consider previous alw
                # so we need to add elements from start to i+1 in our subset arr
                if palindrom(s[:i+1]):
                    backtrack(s[i+1:],subset+[s[:i+1]],res)
        res =  []
        backtrack(s,[],res)
        return res