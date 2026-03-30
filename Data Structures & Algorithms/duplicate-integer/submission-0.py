class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a new array
        # for each num, check if its in array before putting it in
        # if it is, return True
        # if not, keep adding to loop until end of loop
        num_checked = []
        for num in nums:
            if num in num_checked:
                return True
            num_checked.append(num)
        return False
            

    