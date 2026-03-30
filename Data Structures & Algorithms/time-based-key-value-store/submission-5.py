class TimeMap:

    def __init__(self):
        # initalise an object that can store the key:value along with their timestamp
        self.name_data = {} # stores name:{}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Timestamps come in at increasing order
        # current problem: this gets re-assigned everytime set is called with the same key
        if key in self.name_data:
            self.name_data[key][timestamp] = value
        else:
            self.name_data[key] = {timestamp: value}


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.name_data:
            return ""
        l = list(self.name_data[key].keys())
        res = self.binary_search(l, timestamp)
        print(res)
        if res != -1:
            return self.name_data[key][res]
        return ""

        # Run binary search to find prev_timestamp <= timestamp
        # once found, perform O(1) retrieval from ds


    def binary_search(self, nums, timestamp):
        print(timestamp)
        print(nums)
        l, r = 0, len(nums) -1
        res = -1 # constnalty store the biggest timestamp <= timestamp
        while l<=r:
            mid = (l+r)//2
            if nums[mid] <= timestamp:
                res = nums[mid]
                l = mid + 1
            if nums[mid] > timestamp:
                r  = mid - 1
        return res
            

