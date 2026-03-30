class MyHashMap:

    def __init__(self):
        self.arr = [[] for _ in range(100001)]

    def put(self, key: int, value: int) -> None:
        # pass in the key through the function to get a bucket
        # make sure value isnt already in the bucket
        # insert value in bucket
        # also be able to replace values with same key
        index = key % 100001
        bucket = self.arr[index]
        for i, (k, v) in enumerate(bucket):
            if k == key: # we have found an already defined key therefore replace val
                print(v)
                v = value # replace with new vale
                bucket[i] = [k, v]
                return # exit function
        # if we get here that means we haven't found a corresponding key
        bucket.append([key, value])


    def get(self, key: int) -> int:
        # look for it in hashmap using key
        # if it is in hashmap, return the key along with the value (although here it only wants the val)
        # key is used to get to bucket where the val is stored
        index = key % 100001
        bucket = self.arr[index]
        for i, (k,v) in enumerate(bucket):
            if k==key:
                print(v)
                return v
        return -1 # not found

    def remove(self, key: int) -> None:
        index = key % 100001
        bucket = self.arr[index]
        for i, (k,v) in enumerate(bucket):
            if k==key:
                bucket.remove([k,v])



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)