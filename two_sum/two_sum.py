from typing import List, Dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Since we need to return indices and not just the numbers, we need a hashmap
        # This helps us map numbers back to where they were found in O(1) time.
        processed: Dict[int, int] = dict()

        # We iterate through the numbers list once. As we iterate, we ask if target - num,
        # the other complement, was already processed. If it hasn't then we add the current
        # number and its index, as this helps us keep track of the elements and where they are 
        # when we do find a complement.
        for i, num in enumerate(nums):
            if target - num not in processed:
                processed[num] = i
            else:
                # We return the current index, and the index of the other complement when it is processed.
                return [i, processed[target - num]]
        # Unreachable. Constraints say that there is always at least 1 solution.
        return [] 

# Test cases
# [3, 0]
print(Solution().twoSum([1, 2, 3, 5, 7], 6))
# [2, 1]
print(Solution().twoSum([3, 7, 9, 11, 13], 16))
# [5, 3]
print(Solution().twoSum([2, 4, 6, 8, 10, 12], 20))
# [3, 2]
print(Solution().twoSum([1, 2, 3, 5, 7], 8))

