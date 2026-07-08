class TimeMap:

    def __init__(self):
        self.info = {}
        self.timestamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamp:
            self.timestamp[key] = []
        self.timestamp[key].append(timestamp)
        self.info[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.info:
            return self.info[(key, timestamp)]
        elif key in self.timestamp:
            res = None
            for _ in self.timestamp[key]:
                if _ <= timestamp:
                    res = _
                else:
                    break
            if res is None:
                return ""
            else:
                return self.info[(key, res)]

            # left, right = 0, len(self.timestamp[key]) - 1
            # while left <= right:
            #     mid = left + (right - left) // 2
            #     if self.timestamp[mid] < timestamp:
            #         left = mid + 1
            #     else:
            #         right = mid - 1
            # return self.info[(key, left)]
        else:
            return ""
       
        
