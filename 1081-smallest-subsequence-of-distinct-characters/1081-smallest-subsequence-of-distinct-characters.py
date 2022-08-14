class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = Counter(s)
        seen = set()
        stack = []
        for i in s:
            count[i]-=1
            
            if i in seen:
                continue
            while stack and i < stack[-1]  and count[stack[-1]] > 0:
                elem=stack.pop()
                seen.remove(elem)
            stack.append(i)
            seen.add(i)
        return "".join(stack)