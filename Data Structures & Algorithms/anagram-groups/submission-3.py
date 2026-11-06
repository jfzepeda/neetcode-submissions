class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        res = []

        for w in strs:
            sw = ''.join(sorted(w))
            if (sw in sets):
                sets[sw].append(w)
            else:
                sets[sw] = [w]
        
        for i, v in enumerate(sets):
            res.append(sets[v])

        return res
            
