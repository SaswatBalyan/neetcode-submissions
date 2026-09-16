class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        reverse=[-n for n in nums]
        heapq.heapify(reverse)
        for i in range(k):
            ans = heapq.heappop(reverse)
            
        return -ans
