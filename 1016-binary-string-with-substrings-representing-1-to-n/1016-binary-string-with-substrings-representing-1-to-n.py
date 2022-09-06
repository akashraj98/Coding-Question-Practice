class Solution:
    def queryString(self, s: str, n: int) -> bool:
        res = []
        q = deque(["1"])
        count = 0
        while q:
            d = q.popleft()
            if d not in s:
                return False
            res.append(d)
            count+=1
            if count==n:
                break
            q.append(d+"0")
            q.append(d+"1")
        return True