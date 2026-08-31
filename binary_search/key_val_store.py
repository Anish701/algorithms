from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(dict)
        self.time_arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key][timestamp] = value
        self.time_arr[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        arr = self.time_arr[key]
        mp = self.time_map[key]

        if timestamp in mp:
            return mp[timestamp]

        res = ""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] <= timestamp:
                res = mp[arr[mid]]
                left = mid + 1
            else:
                right = mid - 1
            
        return res