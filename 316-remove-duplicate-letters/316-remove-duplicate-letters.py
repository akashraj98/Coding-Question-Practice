class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occr = {}
        visited = set()
        stack = []
        for i,el in enumerate(s):
            last_occr[el] = i

        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and stack[-1]> s[i] and last_occr[stack[-1]] > i:
                visited.remove(stack.pop())
                    
            stack.append(s[i])
            visited.add(s[i])
        
        return ''.join(stack)
        
        
#     Counter method Apprach 2        
#         count= Counter(s)
#         stack = []
#         seen = set()
        
#         for c in s:
#             count[c]-=1  # don;t forget this
#             if c in seen:
#                 continue
#             while stack and c < stack[-1] and count[stack[-1]] > 0:
#                 elem = stack.pop()
#                 seen.remove(elem)
#             stack.append(c)
#             seen.add(c)
#         return "".join(stack)