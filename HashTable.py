class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = [[] for i in range(self.size)]

    # O(n)
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    # O(n)
    def add(self, key, value):
        h = self.get_hash(key)
        found = False

        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][i] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    # O(n)
    def get(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    # O(n)
    def update(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is not None:
            for key_value in self.arr[h]:
                if key_value[0] == key:
                    key_value[1] = value
                    return True

    # O(n)
    def get_index(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return h

    # O(1)
    def return_size(self):
        return self.size

    # O(1)
    def return_keys(self):
        return self.arr
