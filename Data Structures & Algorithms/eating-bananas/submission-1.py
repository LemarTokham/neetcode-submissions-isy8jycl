import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        hours = 0
        bananaRate = r
        while l <= r:
            k = (l + r) // 2
            print(k)
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
                print(hours)
            if hours > h:
                l = k + 1
            elif hours <= h:
                r = k - 1
                bananaRate = k
        return bananaRate