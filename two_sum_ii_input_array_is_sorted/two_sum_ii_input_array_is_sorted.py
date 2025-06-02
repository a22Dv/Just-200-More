from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lft = 0
        rgt = len(numbers) - 1

        # The core premise is that it is sort of like a hot-cold game.
        # We can take advantage of the fact that the arrays are sorted.
        # If the sum is less, we know we need more, so we add to the left pointer
        # so that it gets taken to a higher number.
        # If it is less, then we move the right pointer down to a lower number, this makes it
        # so we converge right to the correct indices, as left and right
        # were already at their highest and lowest initially.
        while True:
            ptr_sum = numbers[lft] + numbers[rgt]
            if target < ptr_sum:
                rgt -= 1
            elif target > ptr_sum:
                lft += 1
            else:
                return [lft + 1, rgt + 1]

# [4, 5]
print(Solution().twoSum([1, 3, 5, 6, 9, 11], 15))