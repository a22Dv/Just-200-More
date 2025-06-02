from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We initialize the product to all 1s.
        product = [1 for _ in range(len(nums))]

        # As we go to a direction we store an intermediate product.
        intermediate = nums[0]

        # The key insight is that the product of the array is just the
        # product of left and rights, as multiplication is already
        # commutative, the order doesn't matter.

        # We start at 1, with intermediate already equal to the number before.
        # This means as we pass, the product is offset, excluding its own.
        for i in range(1, len(nums)):
            product[i] *= intermediate
            intermediate *= nums[i]

        # We do the same procedure, but now with the other direction.
        intermediate = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            product[i] *= intermediate
            intermediate *= nums[i]
        return product


# [24, 12, 8, 6]
print(Solution().productExceptSelf([1, 2, 3, 4]))
