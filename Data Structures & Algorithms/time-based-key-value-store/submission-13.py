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
        # if (key, timestamp) in self.info:
        #     return self.info[(key, timestamp)]
        # elif key in self.timestamp:
        
            # res = None
            # for _ in self.timestamp[key]:
            #     if _ <= timestamp:
            #         res = _
            #     else:
            #         break
            # if res is None:
            #     return ""
            # else:
            #     return self.info[(key, res)]
        
        if key not in self.timestamp:
            return ""

        arr = self.timestamp[key]

        if arr[0] > timestamp:
            return ""

        left, right = 0, len(arr) - 1
        # while left < right:
        #     mid = left + (right - left + 1) // 2
        #     if arr[mid] <= timestamp:
        #         left = mid 
        #     else:
        #         right = mid - 1
        # return self.info[(key, arr[left])]

        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return self.info[(key, arr[ans])]

        # else:
        #     return ""
       
        
