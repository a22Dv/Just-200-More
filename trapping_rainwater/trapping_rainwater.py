from typing import List


class Solution:
    def trap_dp(self, height: List[int]) -> int:
        # Initialize variables.
        height_len = len(height)
        max_height = 0
        water_l = [0 for _ in range(height_len)]
        water_r = [0 for _ in range(height_len)]

        # We go pass from the left.
        for i in range(height_len):
            if height[i] > max_height:
                max_height = height[i]
            diff = max_height - height[i]
            water_l[i] = diff

        # We pass from the right.
        max_height = 0
        for i in range(height_len - 1, -1, -1):
            if height[i] > max_height:
                max_height = height[i]
            diff = max_height - height[i]
            water_r[i] = diff

        # We return the sum of the minimum of both arrays.
        return sum(min(wl, wr) for wl, wr in zip(water_l, water_r))

    def trap_2ptr(self, height: List[int]) -> int:
        # We initialize variables.
        len_map = len(height)
        left = 0
        right = len_map - 1
        max_left = 0
        max_right = 0
        water = 0

        # Loop until the pointers don't overlap.
        while left < right:

            # Here left is lower. And so max_left is what will limit the water.
            if height[left] < height[right]:
                # We don't need to add to the water if it was the highest as nothing can contain it on the left side.
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            # Here right is lower. And so max_right is what will limit the water.
            else:
                # We don't need to add to the water if it was the highest as nothing can contain it on the right side.
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1
        return water


# 6
print(Solution().trap_2ptr([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
print(Solution().trap_dp([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
