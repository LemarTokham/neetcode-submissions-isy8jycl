class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # returning a number and the modified nums gets check automatically
        repeats = []
        for num in nums:
            if val != num:
                repeats.append(num)
        
        for i in range(len(repeats)):
            nums[i] = repeats[i]

        n = len(repeats)
        nums = nums[:n] # :3 repeats[2,3,4], nums[2,3,4,3,4]

        return n
        


