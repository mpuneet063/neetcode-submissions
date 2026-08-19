class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        value_list = self.dic[key]

        l, r = 0, len(value_list) - 1
        res = ""

        while l <= r:
            m = (l+r)//2

            if value_list[m][1] <= timestamp:
                res = value_list[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res