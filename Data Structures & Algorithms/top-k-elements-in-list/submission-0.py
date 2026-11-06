class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        top_k = sorted(map, key=map.get, reverse=True)[:k]
        return top_k