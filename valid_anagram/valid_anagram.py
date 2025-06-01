class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Strings of different lengths can never be complete anagrams of each other.
        if len(s) != len(t):
            return False
        # We need to keep track of the letter counts of the anagrams.
        freqs = [0 for _ in range(26)]

        # This is needed to normalize the ASCII range to map to their
        # respective positions in the alphabet for `freqs`, 0-25
        transform = ord("a")

        # We loop through the first string, adding to the frequency of the respective
        # letters.
        for c in s:
            freqs[ord(c) - transform] += 1

        # We loop through the second string, subtracting from the frequency of the respective
        # letters. Crucially, if anything goes below 0, it quits immediately and returns False.
        # We only need one letter to not match to declare the entire string an invalid anagram.
        for c in t:
            freqs[ord(c) - transform] -= 1
            if freqs[ord(c) - transform] < 0:
                return False
        # We only check for negatives since to have an extra letter (+),
        # you must have taken it away from another letter's spot (-)
        # The only way to get only positives is if the strings aren't the same length which is
        # taken care of earlier.
        return True

# Test cases
# True
print(Solution().isAnagram("helloworld", "worldhello"))
# False
print(Solution().isAnagram("attack", "tgacka"))
# True
print(Solution().isAnagram("thisis", "isisth"))
# False
print(Solution().isAnagram("python", "omhtyp"))

