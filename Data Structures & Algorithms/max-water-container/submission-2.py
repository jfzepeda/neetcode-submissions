class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights)
        glob_max = 0

        for i, v1 in enumerate(heights):

            for inv_j in range(l-1,0,-1):
                v2 = heights[inv_j]

                if i >= inv_j : break

                producto = min(v1,v2) * (inv_j - i)
                glob_max = max(producto, glob_max)

                if v1 < v2: break
        
        return glob_max