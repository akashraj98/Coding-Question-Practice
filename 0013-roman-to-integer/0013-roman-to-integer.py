class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {"I":1, "IV":4,
                "V":5, "IX":9, "X":10,
                "XL":40, "L":50, "XC":90, "C":100,
                "CD":400, "D":500,"CM":900, "M":1000
               }
        start = 0
        end = len(s)
        res = 0
        while start < end:
            if s[start:start+2] in hmap:
                res+= hmap[s[start:start+2]]
                start = start+2
            elif s[start:start+1] in hmap:
                res+= hmap[s[start:start+1]]
                start = start+1
        return res