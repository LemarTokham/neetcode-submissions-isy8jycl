class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        l = 0
        r = len(s) - 1
        for i in range(len(s)):
            print(s[i])
            if r < l: # Must be a palindrone if pointers have crossed each other
                return True
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower(): # Letters dont match do not palindrome
                print(s[l], s[r])
                return False
            # Letters match so increment both points
            l += 1
            r -= 1
        return True