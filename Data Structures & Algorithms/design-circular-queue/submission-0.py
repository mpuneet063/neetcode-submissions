class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque(maxlen=k)
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.queue) != 0:
            self.queue.popleft()
            return True
        else:
            return False

    def Front(self) -> int:
        return self.queue[0] if self.queue else -1

    def Rear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()