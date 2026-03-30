class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        lMax = height[l]
        rMax = height[r]
        while l < r:
            print(l, r)
            if lMax < rMax:
                calc = lMax - height[l]
                lMax = max(lMax, height[l])
            elif rMax < lMax:
                calc = rMax - height[r]
                rMax = max(rMax, height[r])
            else:
                calc = min(rMax,lMax) - height[r]
                rMax = max(rMax, height[r])

            if rMax > lMax:
                l += 1
            else:
                r -= 1

            if calc > 0:
                res += calc
            
        return res
