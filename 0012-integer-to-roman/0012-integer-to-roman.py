class Solution:
    def intToRoman(self, num: int) -> str:
        hmap = {1:"I", 4:"IV",
                5:"V", 9:"IX", 10:"X",
                40:"XL", 50:"L", 90:"XC", 100:"C",
                400:"CD", 500:"D",900:"CM", 1000:"M"
               }
        def findPrev(n):
            prev = 0
            for k in hmap:
                if k<=n:
                    prev = k
                else:
                    return prev
            return prev
        res = ""
        while num:
            prev = findPrev(num)
            prev_freq = num //prev
            num = num% prev
            res += hmap[prev]* prev_freq
        return res