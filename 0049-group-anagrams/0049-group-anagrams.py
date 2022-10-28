class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}
        res = []
        for i in strs:
            si = "".join(sorted(i))
            if si in h_map:
                h_map[si] += [i]
            else:
                h_map[si] = [i]
                
        # for k,v in h_map.items():
        #     res.append(v)
        return h_map.values()
            
        