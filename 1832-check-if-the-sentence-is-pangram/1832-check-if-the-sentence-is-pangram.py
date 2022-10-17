class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter_map = {}
        for l in sentence:
            letter_map[l] = letter_map.get(l,0)+1
        # print(letter_map)
        return(len(letter_map)==26)
            
        
        