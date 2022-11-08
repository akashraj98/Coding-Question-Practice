class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ""
        flag =1
        for n in str(num):
            if n=="6" and flag:
                res+="9"
                flag = 0
                continue
            res+=n
        return int(res)