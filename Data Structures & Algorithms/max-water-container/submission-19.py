class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # notes:
        # array in 2 pointers doesnt have to be sorted
        # 2 pointers is used when trying to find a pair or more of numbers in an array where theres also a sort of relationship
        # take both pos, use the smallest of the 2 to find your area
        left, right = 0, len(heights) - 1
        max_area = 0
        area = 0
        control = 0
        while left < right:
            # find which is smaller
            # compute area
            # moe pointer that had smaller height back/forth
            if heights[left] < heights[right]:
                control = heights[left]
                area = control * (right - left)
                left += 1
            else: # greater than or same - move the right backwards
                control = heights[right]
                area = control * (right - left)
                right -= 1
            
            max_area = max(max_area, area)
            print(max_area)

        return max_area












