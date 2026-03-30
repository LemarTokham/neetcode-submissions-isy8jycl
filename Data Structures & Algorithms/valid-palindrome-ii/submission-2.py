class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointers comapring letters
        # if one letter differs, let it go
        # if more than one, it can't be
        l, r = 0, len(s) - 1
        palin = True
        res1 = False
        res2 = False
        while l <= r:
            if s[l] != s[r]:
                return self.is_palin(s[l+1:r+1]) or self.is_palin(s[l:r])
            l += 1
            r -= 1

        return True
    
    def is_palin(self,s):
        print(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True




