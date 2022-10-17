class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter_map = {}
        count = 0
        for l in sentence:
            val = letter_map.get(l,0)
            if val==0:
                count+=1
            letter_map[l] = val +1
        return(count==26)
            
        
        