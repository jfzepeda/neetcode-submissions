class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        map = {}
        nums.sort()

        for i, v in enumerate(nums):
            map[v] = map.get(v-1,0) + 1

        return max(map.values(), default=0)