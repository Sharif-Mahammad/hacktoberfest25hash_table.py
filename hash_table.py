class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return len(key) % self.size  # ❌ Weak hash, causes collisions

    def insert(self, key, value):
        index = self.hash_func(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_func(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

h = HashTable(5)
h.insert("apple", 10)
h.insert("mango", 20)
print(h.get("mango"))  # Expected 20, Got None (collision)
