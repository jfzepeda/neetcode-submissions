class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        jump = l
        dir = -1
        idx = 0
        min_val = nums[0]

        if nums[-1] >= min_val:
            return min_val
        
        min_val = nums[-1]

        for _ in range(10):
            jump = max(jump//2,1)
            next_index = dir*jump+idx
            print(dir,jump,idx)
            next_val = nums[next_index]

            if next_val > min_val:
                # ir a la derecha
                dir = 1
            elif next_val < min_val:
                # ir a la izquierda
                min_val = next_val
                dir = -1
            elif next_val == min_val:
                if nums[next_index-1] < min_val:
                    dir = -1
                else:
                    break
            idx = next_index
        
        
        return min_val