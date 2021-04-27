# d = {
#     "banana": "is a fruit"
# }

class Dict:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
​
    def hash_func(self, key):
        bytes_str = key.encode()
        num = 0
        for byte in bytes_str:
            num += byte
        return num % self.capacity
​
    def insert(self, key, value):
        # hash the key            
        index = self.hash_func(key)
        self.storage[index] = (key, value)
​
    def get(self, key):
        # has the key to get the index
        index = self.hash_func(key)
        return self.storage[index][1]
​
    def delete(self, key):
        # has the key to get the index
        index = self.hash_func(key) 
        self.storage[index] = None
​
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
​
d = Dict(8)
​
d['apple'] = 'is a fruit'
d['banana'] = 'is also fruit'
d['cucumber'] = 'is a vegetable'
d['peach'] = 'This is definitely not a banana'
​
print(d['apple'])
print(d['banana'])