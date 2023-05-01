class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.count = 0
        

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            self.count+=1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        self.set.remove(val)
        self.count-=1
        return True
        

    def getRandom(self) -> int:
        import random
        return random.choice(list(self.set))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()