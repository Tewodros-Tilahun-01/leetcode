class RandomizedSet:

    def __init__(self):
        self.hashmap = set()
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap.add(val)
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        self.hashmap.remove(val)
        self.size -= 1
        return True

    def getRandom(self) -> int:
        index = random.randint(0, self.size-1) 
        rand = list(self.hashmap)
        return rand[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()