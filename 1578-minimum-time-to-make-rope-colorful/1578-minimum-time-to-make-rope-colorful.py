class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Two pointer compare which one to remove
        time = 0
        left = 0
        right = 1
        while right < len(colors):
            if colors[left] != colors[right]:
                left = right
                right+=1
            else:
                if neededTime[left]< neededTime[right]:
                    time += neededTime[left]
                    left = right
                    right+=1
                else:
                    time+=neededTime[right]
                    right+=1
        return time