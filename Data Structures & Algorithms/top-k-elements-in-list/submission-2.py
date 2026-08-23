class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = defaultdict(int)
        for num in nums:
            dictt[num] += 1
        
        sorted_dict = sorted(dictt, key=lambda x: -dictt[x])
        return sorted_dict[:k]