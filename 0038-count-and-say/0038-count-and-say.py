class Solution:
    def countAndSay(self, n: int) -> str:
        # 1
        # 1 1
        # 2 1
        # 1 2 1 1
        # 1 1 1 2 2 1
        # 3 1 2 2 1 1
        if n==1:
            return "1"
        
        x = self.countAndSay(n-1)
        s = ""
        y = x[0]
        cnt = 1
        for xi in x[1:]:
            if xi ==y:
                cnt+=1
            else:
                s+=str(cnt)
                s+=str(y)
                y = xi
                cnt =1
        s+=str(cnt)
        s+=str(y)
        return s
        
        