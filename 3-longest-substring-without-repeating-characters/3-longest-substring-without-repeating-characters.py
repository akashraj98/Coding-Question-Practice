class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        start = 0
        end = start+1
        N = len(s)
        m_count = 1
        
        for i in range(end,N+1):
            if len(s[start:i]) == len(set(s[start:i])):
                m_count = max(m_count,len(s[start:i]))
            else:
                #shrink from start
                start+=1

        return m_count
            
        