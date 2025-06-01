import heapq
from typing import List, Dict, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We need a way to keep track of the counts for each number.
        counts: Dict[int, int] = dict()

        # We go through nums and increment the counts.
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        # A min-heap.
        heap: List[Tuple[int, int]] = []

        # We then go through the counts, and use a heap to get the top-k.
        for num, count in counts.items():
            # Heap is smaller than k.
            if len(heap) < k:
                # We just push.
                heapq.heappush(heap, (count, num))
            # Heap is already of size k.
            elif heap[0][0] < count:
                # We replace the root node and let the heap
                # restructure to keep the min-heap property.
                heapq.heapreplace(heap, (count, num))
        # Return the integer component.
        return [v[1] for v in heap]
    
# Test cases
# [3, 1]
print(Solution().topKFrequent([1,1,1,2,3,3,4], 2))
# [3, 2, 1]
print(Solution().topKFrequent([1,1,1,2,2,2,2,3,3,4], 3))
# [4]
print(Solution().topKFrequent([1,1,1,2,3,3,4,4,4,4], 1))
# [1, 8]
print(Solution().topKFrequent([1,1,1,1,2,3,3,3,8,8,8,8,8], 2))
