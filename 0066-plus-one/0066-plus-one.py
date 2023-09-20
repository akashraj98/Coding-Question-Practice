class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        carry=1
        i = len(digits)-1
        while carry:
           
            val=digits[i]+1
            if val>9:
                digits[i]=0
                carry=1
                i-=1
                if i not in range(0,len(digits)-1):
                    digits= [1]+digits
                    return digits
            else:
                digits[i]=val
                return digits
        
            
        