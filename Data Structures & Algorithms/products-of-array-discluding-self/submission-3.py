class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        producto = 1
        res = []
        zeros = nums.count(0)

        if zeros > 1:
            for i in nums:
                res.append(0)
            return res


        for n in nums:
            if n != 0:
                producto *= n
        
        for i in nums:
            if i == 0:
                res.append(producto) 
            else:
                res.append((1-zeros)*producto//i) 
        
        return res