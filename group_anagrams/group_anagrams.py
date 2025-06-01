from typing import List, Dict, Tuple

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        TRANSFORM: int = ord("a")
        # We need a way to keep track of the frequencies we have seen.
        frequencies: Dict[Tuple[int, ...], List[str]] = dict()
        # As we go through the list, we get their frequency.
        for string in strs:
            frequency: List[int] = [0 for _ in range(26)]
            for c in string:
                frequency[ord(c) - TRANSFORM] += 1
            # Canonical representation.
            tuple_freq: Tuple[int, ...] = tuple(frequency)
            # We then create a new entry or add them to the existing entry
            if tuple_freq in frequencies:
                frequencies[tuple_freq].append(string)
            else:
                frequencies[tuple_freq] = [
                    string,
                ]
        # We then get all the values and return them.
        return [v for v in frequencies.values()]

# Test cases
# [["ab", "ba"], ["cd", "dc"]]
print(Solution().groupAnagrams(["ab", "cd", "ba", "dc"]))
# [["agh", "hga"], ["cda", "dac"]]
print(Solution().groupAnagrams(["agh", "cda", "dac", "hga"]))
# [["real", "lear"], ["rac", "car"]]
print(Solution().groupAnagrams(["real", "rac", "car", "lear"]))
# [["abc", "cba"], ["def", "fed"], ["ghi", "igh"]]
print(Solution().groupAnagrams(["abc", "cba", "def", "fed", "ghi", "igh"]))