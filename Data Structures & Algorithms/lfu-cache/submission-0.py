from collections import OrderedDict, defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}  # key -> value
        self.key_to_freq = {}  # key -> frequency
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> OrderedDict of keys
        self.min_freq = 0

    def _update_freq(self, key: int) -> None:
        """Promote a key's frequency by 1 and move it in OrderedDicts."""
        freq = self.key_to_freq[key]
        self.key_to_freq[key] = freq + 1

        # Remove from old frequency group
        del self.freq_to_keys[freq][key]

        # If old frequency group was the minimum and is now empty, advance min_freq
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1

        # Add to new frequency group (at the end, marking it MRU for this frequency)
        self.freq_to_keys[freq + 1][key] = True

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        # Evict LRU key from the lowest frequency group if full
        if len(self.key_to_val) >= self.capacity:
            # popitem(last=False) pops the oldest/least recently used key in min_freq group
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]

        # Insert new key
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = True
        self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)