class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                current_area = heights[l] * (r - l)
                print(current_area)
                l += 1
            else:
                current_area = heights[r] * (r - l)
                r = r - 1
                print(current_area)
            if current_area > max_area:
                print("ho")
                max_area = current_area
            
        return max_area