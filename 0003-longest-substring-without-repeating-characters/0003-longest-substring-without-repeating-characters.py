class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Use two pointer extend from right and shrink from left
        #place both in start first
        res = 0
        l=0
        for r in range(len(s)+1):
            if len(s[l:r]) == len(set(s[l:r])):
                res = max(res,r-l)
            else:
                l+=1
        return res
            
            