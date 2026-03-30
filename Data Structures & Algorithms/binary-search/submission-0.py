class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import math
        upperBound = len(nums) - 1
        lowerBound = 0
        midpoint = math.floor((upperBound - lowerBound) / 2)
        while True:
            if lowerBound > upperBound or upperBound < lowerBound:
                return -1
            if nums[midpoint] == target:
                return midpoint
            elif target < nums[midpoint]:
                upperBound = midpoint - 1
            else:
                lowerBound = midpoint + 1
            midpoint = math.floor((upperBound - lowerBound) / 2) + lowerBound
        return -1