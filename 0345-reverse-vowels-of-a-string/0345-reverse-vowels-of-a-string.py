class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s)-1
        vowels = ['a','e','i','o','u']
        s = [i for i in s]
        while start<end:
            if s[start].lower() not in vowels:
                start+=1
            elif s[end].lower() not in vowels:
                end-=1
            else:
                s[start],s[end] = s[end],s[start]
                start+=1
                end-=1
        return "".join(s)