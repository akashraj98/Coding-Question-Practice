class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        c_sum = 0  # running sum
        m_sum = arr[0] # max till now
        for i in range(len(arr)):
            c_sum+=arr[i]
            m_sum = max(c_sum,m_sum)
            if c_sum < 0:
                c_sum = 0
        return m_sum
        
        
        
        
        
        # c_sum = 0
        # n = len(arr)
        # m_sum = arr[0]
        # for i in range(n):
        #     c_sum+=arr[i]
        #     m_sum = max(m_sum,c_sum)
        #     if c_sum<0:
        #         c_sum = 0
        # return m_sum
