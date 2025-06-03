from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_count = len(prices)
        # Handle edge case.
        if price_count < 2:
            return 0

        # Initialize variables.
        profit = 0
        left = 0
        right = 1

        # Core logic. To maximize profit we want the lowest price to buy, and the
        # highest price to sell. To do this all we do is let a left pointer
        # act as the buy, the right as sell. We let right push forward, changing our
        # profit maximum as it goes. Crucially, if we find a price lower than the one in
        # our left (buy) pointer, we move our left buy pointer to the same position of the
        # right. Giving us a more advantageous position. And this goes on until right reaches 
        # the end.
        while right < price_count:
            profit = max(profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit
