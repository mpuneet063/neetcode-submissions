class FreqStack:

    def __init__(self):
        self.freq = collections.defaultdict(int)
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        new_freq = self.freq[val]

        self.group[new_freq].append(val)

        self.max_freq = max(self.max_freq, new_freq)

    def pop(self) -> int:
        if self.max_freq == 0:
            return 

        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group.get(self.max_freq):
            del self.group[self.max_freq]
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()