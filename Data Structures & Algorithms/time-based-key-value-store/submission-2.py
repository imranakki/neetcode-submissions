from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.mp = {}
        self.val = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = SortedList([])
        self.mp[key].add(timestamp)
        self.val[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        idx = self.mp[key].bisect_right(timestamp)
        if(idx == 0):
            return ""
        return self.val[(key, self.mp[key][idx - 1])]
