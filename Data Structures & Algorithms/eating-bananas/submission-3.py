class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles) # used for binary search
        res = 0
        l = 1
        r = maxPile
        while l <= r:
            mid = (l + r) // 2
            calc = 0
            for pile in piles:
                calc += int(math.ceil(pile / mid))

            if calc > h: # Invalid - increae banan eating rate
                l = mid + 1
            else: # See if we can eat less banans
                r = mid - 1
                res = mid
            print(mid)
            


        return res
