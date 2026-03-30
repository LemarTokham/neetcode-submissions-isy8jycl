class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        l = 0
        r = len(nums) - 1
        res = 1001
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < res:
                res = nums[mid]
            if nums[mid] >= nums[l]:
                if nums[mid] > nums[r]: # We need to look in right list
                    l = mid+1
                else:
                    r = mid - 1 # List must be sorted if r points to bigger num
            elif nums[mid] <= nums[l]:
                r = mid-1
        return res
            

                