class Solution:
    def checkValidString(self, s: str) -> bool:
        l_low = l_high = 0
        for c in s:
            if c=='(':
                l_low+=1
                l_high+=1
            elif c==')':
                l_low-=1
                l_high-=1
            else:
                l_low-=1
                l_high+=1
            if l_high<0:
                return False
            l_low = max(0,l_low)
        return l_low==0