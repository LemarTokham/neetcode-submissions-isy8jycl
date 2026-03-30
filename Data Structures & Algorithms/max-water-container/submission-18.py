class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights)
        r = n - 1
        maxArea = 0
        while l <= r:
            area = min(heights[l], heights[r]) * (r - l) 
            maxArea = max(area, maxArea)
            if heights[r] > heights[l]:
                l += 1
                continue
            print(area, r, l, heights[r])
            r -= 1

        return maxArea