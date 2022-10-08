from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.dict = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.dict[start] = self.dict.get(start,0)+1
        self.dict[end] = self.dict.get(end,0)-1
        res=curr = 0
        for val in self.dict.values():
            curr+=val
            res = max(res,curr)
        return res
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)