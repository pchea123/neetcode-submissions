class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        sorted_counts = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        # how do i get this to return just the first k elements
        return list(sorted_counts)[0:k]
