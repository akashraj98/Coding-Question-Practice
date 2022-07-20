class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        c_sum = 0
        n = len(arr)
        m_sum = arr[0]
        start =0
        end =0
        while end < n:
            c_sum+=arr[end]
            m_sum = max(m_sum,c_sum)
            if c_sum <0:
                c_sum =0
                start+=1
            end+=1
        return m_sum
