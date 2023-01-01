from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split(' ')
        p_loc = defaultdict(list)
        s_loc = defaultdict(list)
        for i,p in enumerate(pattern):
            p_loc[p].append(i)
            
            
        for j,s in enumerate(s_split):
            s_loc[s].append(j)
        pval = list(p_loc.values())
        sval = list(s_loc.values())
        if len(p_loc.values()) != len(s_loc.values()):
            return False
        for i in range(len(s_loc.values())):
            if pval[i]!= sval[i]:
                return False
        return True
            
        
                
            
            