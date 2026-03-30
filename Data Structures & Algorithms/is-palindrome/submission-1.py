class Solution:
    def isPalindrome(self, s: str) -> bool:
        # covert str to valid str
        t = []
        for char in s:
            if char.isalpha() or char.isdigit():
                t.append(char)
        new_s = ''.join(t).lower()
        # actual palindrone
        left = 0
        right = len(new_s) - 1
        while left < right:
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
