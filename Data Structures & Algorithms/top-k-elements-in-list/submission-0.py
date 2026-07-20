class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        res = sorted(seen, key = seen.get, reverse=True)[0:k]

        return res
        