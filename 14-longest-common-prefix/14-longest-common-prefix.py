class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        longest = ""
        i=0
        while i<len(first):
            i= i+1
            for s in strs:
                if first[:i] == s[:i]:
                    pass
                else:
                    return longest
            longest = s[:i]
        return first[:i+1]

        