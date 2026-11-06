class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map = {}
        l = len(nums)
        res = set()

        for i in range(l):
            comp = 0 - nums[i]
            map[comp] = i
        
        for i in range(l-1):
            
            for j in range(i+1, l):
                comp = nums[i] + nums[j]
                
                idx = map.get(comp, i)
                
                if  (idx != i) and (idx != j):
                    s = tuple(
                        sorted(
                            [nums[i],nums[j],nums[idx]]
                        )
                    )
                    res.add(s)
        
        return list(res)

            
