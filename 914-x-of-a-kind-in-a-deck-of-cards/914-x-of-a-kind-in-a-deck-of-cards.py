class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from math import gcd
        count = Counter(deck)
        return reduce(gcd,count.values())>=2
#         s = set(f_c.values())
#         if len(s) ==1:
#             return True
#         else:
#             ms=min(s)
#             for el in s:
#                 if el%ms != 0:
#                     return False
#             return True
        