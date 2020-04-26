class LRUCache:

    def __init__(self, capacity: int):
        self.order = []
        self.capacity=capacity
        self.dict = dict()
        self.next, self.before = {}, {}
        self.head, self.tail = '#', '$'
        self.connect(self.head, self.tail)
    def connect(self,a,b):
        self.next[a], self.before[b] = b, a

    def get(self, key: int) -> int:
        if key in self.dict:
            self.order.remove(key)
            self.order.append(key)
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.order.remove(key)
            self.order.append(key)
            self.dict[key] = value
        else:
            self.dict[key] = value
            self.order.append(key)
        if len(self.order) >self.capacity:
            val = self.order.pop(0)
            if val not in self.order:
                del self.dict[val]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
