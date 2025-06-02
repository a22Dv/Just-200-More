class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Get the limits.
        control = (ord("a"), ord("z"), ord("0"), ord("9"))
        string = ""
        
        # Filter string.
        for c in s.lower():
            if control[0] <= ord(c) <= control[1] or control[2] <= ord(c) <= control[3]:
                string += c
        string_len = len(string)

        # Return False if both pointers don't match.
        for i in range(string_len):
            if string[i] != string[string_len - 1 - i]:
                return False
        return True

# False
print(Solution().isPalindrome("2a3re3a"))