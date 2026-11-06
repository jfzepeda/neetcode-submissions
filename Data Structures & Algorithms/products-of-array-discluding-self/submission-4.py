class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        producto = 1
        zeros = 0
        res = []

        for n in nums:
            if n == 0:
                zeros += 1
            else :
                producto *= n
        
        if zeros > 1:
            for i in nums:
                res.append(0)

        else:
            for i in nums:
                if i == 0:
                    res.append(producto) 
                else:
                    res.append((1-zeros)*producto//i) 
        
        return res