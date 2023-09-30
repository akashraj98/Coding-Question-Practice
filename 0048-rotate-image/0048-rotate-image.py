class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose and reverse
        for i in range(1,len(matrix[0])):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                
        # reverse the matrix row
        def reverse(arr):
            i=0
            j=len(arr)-1
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            
        for row in matrix:
            reverse(row)
    
        
        