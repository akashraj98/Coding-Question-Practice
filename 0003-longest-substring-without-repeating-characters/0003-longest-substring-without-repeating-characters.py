class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        res = 1
        i = 0
        while i< len(s) and res+1<= len(s):
            substring = s[i:i+res+1]
            # print(substring)
            if len(substring) == len(set(substring)) and len(substring)> res:
                res+=1
                i=0
            else:
                i+=1
        return res
                
        