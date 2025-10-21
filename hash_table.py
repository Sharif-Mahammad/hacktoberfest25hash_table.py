class HashTable:
    def _init_(self, size):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return sum(ord(c) for c in key) % self.size  # ✅ Better hash

    def insert(self, key, value):
        index = self.hash_func(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))  # ✅ Handle collisions

    def get(self, key):
        index = self.hash_func(key)
        if self.table[index]:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

h = HashTable(5)
h.insert("apple", 10)
h.insert("mango", 20)
print(h.get("mango"))  # ✅ Output: 20
