class Solution:
    def findMin(self, nums: List[int]) -> int:
        jump = len(nums)
        dir = -1
        idx = 0
        min_val = nums[0]

        if nums[-1] >= min_val:
            return min_val
        else:
            min_val = nums[-1]

        while True:
            jump = max(jump//2,1)
            next_index = dir*jump+idx
            next_val = nums[next_index]

            if next_val > min_val:
                dir = 1
                
            elif next_val < min_val:
                min_val = next_val
                dir = -1

            elif nums[next_index-1] > min_val:
                    break
            
            idx = next_index
        
        return min_val