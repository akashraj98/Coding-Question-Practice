class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c_mag = Counter(magazine)
        for i in ransomNote:
            if i in c_mag and c_mag[i]>0:
                c_mag[i]-=1
            else:
                return False
        return True