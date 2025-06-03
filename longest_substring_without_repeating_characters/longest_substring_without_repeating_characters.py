from typing import Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Initialize variables.
        max_distance = 0
        start = 0
        end = 0

        # Keep track of current characters.
        chars: Set[str] = set()
        len_s = len(s)

        while end < len_s:
            # s[end] is a unique character. So we push forward.
            if s[end] not in chars:
                chars.add(s[end])
                end += 1
            # It is not. So we move the start pointer forward until it is.
            else:
                chars.remove(s[start])
                start += 1
            # Update distance for each iteration.
            max_distance = max(max_distance, end - start)
        return max_distance
