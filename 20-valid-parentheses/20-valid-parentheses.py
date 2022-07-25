class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid =['()','{}','[]']
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
                continue
            if (stack[-1]+s[i]) in valid:
                stack.pop(-1)
            else:
                stack.append(s[i])
        return len(stack)==0