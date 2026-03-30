class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # find k
        k =0
        for num in nums:
            if num != val:
                k += 1 
        # two pointers apprach
        l, r = 0, len(nums) - 1
        while l<r:
            if nums[l] != val: # l will be used to replace val with non-val nums
                l+=1
                continue
            
            if nums[r] != val:
                print(nums[l], nums[r])
                nums[l] = nums[r] # move non-val to front
                print(nums[l], nums[r])
                l+=1
            
            r -= 1



        print(k)


        return k
            
            