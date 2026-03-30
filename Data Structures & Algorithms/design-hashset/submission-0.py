class MyHashSet:
    # a hashtable is a collection of indexes, where each index is mapped to a key in the hashtable
    
    def __init__(self):
        self.arr = [[]] * 10001

    def add(self, key: int) -> None:
        # could make a hash function but this really only works if we know already how big the array will be as we can't add to an index we don't have
        # find index of where to store val
        # check its not already there
        # add it in
        index = key % 10001
        if key not in self.arr[index]:
            self.arr[index].append(key)
        

    def remove(self, key: int) -> None:
        index = key % 10001
        if key in self.arr[index]: # Check if in bucket
            self.arr[index].remove(key) 
        

    def contains(self, key: int) -> bool:
        index = key % 10001
        return key in self.arr[index] 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)