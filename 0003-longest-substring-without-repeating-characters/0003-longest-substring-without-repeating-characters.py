class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        mlen = 1
        start =0
        # end =1
        for i in range(len(s)+1):
            if len(s[start:i]) == len(set(s[start:i])):
                mlen = max(mlen,len(s[start:i]))
            else:
                start+=1
        return mlen