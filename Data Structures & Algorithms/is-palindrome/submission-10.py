class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not len(s):
            return false
        s = s.lower()
        s = s.replace(" ", "")
        newS = ""
        # Convert s to only have alphanumeric
        for char in s:
            if char.isalnum():
                newS += char
        print(newS)
        x = 0
        y = len(newS) -1
        for i in range(len(newS)):

            print(x, y)
            if x == y or x > y: # Same position
                print(x, y)
                return True
            if newS[x] != newS[y]: # Different letters mean not palindrome
                return False
            x = x + 1
            y = y - 1
        return True