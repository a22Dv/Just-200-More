from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        # We turn the numbers into a set for quick membership tests.
        num_set = set(nums)

        # We iterate through the set
        for n in num_set:
            count = 1
            # This is the key insight, for any starting sequence, n - 1 won't be in the set.
            # This allows us to pinpoint the start.
            if n - 1 not in num_set:
                # This inner loop then goes until n is NOT in the set. At which point
                # we now know how long is the longest consecutive sequence.
                while True:
                    if n + count in num_set:
                        count += 1
                        continue
                    else:
                        break
                # Store the largest.
                if count > longest:
                    longest = count
        return longest

# 4
print(Solution().longestConsecutive([10, 20, 21, 4, 2, 1, 3]))