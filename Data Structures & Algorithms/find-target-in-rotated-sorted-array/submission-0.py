class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find cut by using binary search
        # if the mid val is > r val, cut is on the right side so move left there and repeat
        # repeat until l and r point to same val
        # goal is to put l where start of list is
        l, r = 0, len(nums) -1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        cut = l
        print(cut)

        def BinarySearch(left, right):
            print(left, right)
            l, r = left, right
            while l<=r:
                m = (l + r) //2
                if nums[m] == target:
                    print(m)
                    return m
                if nums[m] > target: 
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1

            return -1

        res = BinarySearch(0, cut - 1)
        if res != -1:
            return res

        return BinarySearch(cut, len(nums) -1)

        