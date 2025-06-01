from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # We need a set to keep track of the seen digits.
        tracker: Set[int] = set()
        # Iterate through the list,
        for num in nums:
            # Do a membership test and if it is in the set, return true immediately,
            if num in tracker:
                return True
            # We add it to the set since it is unique.
            else:
                tracker.add(num)

        # Return false since we iterated through without seeing a duplicate.
        # Thus, every number is unique.
        return False


# Test cases.

# False
print(Solution().containsDuplicate([1, 2, 3, 4, 5]))
# True
print(Solution().containsDuplicate([1, 34, 32, 32, 5]))
# False
print(Solution().containsDuplicate([100, 24, 3, 44, 5]))
# True
print(Solution().containsDuplicate([1, 45, 39, 45, 5]))
