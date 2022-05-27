class HashMap(object):

    def __init__(self, size):
        self.data = size * [None]
        self.size = size
    
    def hashing_function(self, key):
        hashed_key = int(key) % self.size
        return hashed_key

    def __setitem__(self, key, value):
        hash_key = self.hashing_function(key)
        if self.data[hash_key] is None:
            self.data[hash_key] = value
        else:
            if type(value) == list:
                bucket = []
                bucket.append(self.data[hash_key])
                bucket.append(value)
            else:
                bucket = []
                if type(self.data[hash_key]) == list:
                    for i in self.data[hash_key]:
                        bucket.append(i)
                    bucket.append(value)
                else:
                    bucket.append(self.data[hash_key])
                    bucket.append(value)
                
            self.data[hash_key] = bucket

    def __getitem__(self, key):
        hash_key = self.hashing_function(key)
        return self.data[hash_key]
        
