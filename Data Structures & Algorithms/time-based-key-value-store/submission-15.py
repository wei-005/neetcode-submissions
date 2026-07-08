# class TimeMap:

#     def __init__(self):
#         self.info = {}
#         self.timestamp = {}

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.timestamp:
#             self.timestamp[key] = []
#         self.timestamp[key].append(timestamp)
#         self.info[(key, timestamp)] = value

#     def get(self, key: str, timestamp: int) -> str:
        
#         if key not in self.timestamp:
#             return ""

#         arr = self.timestamp[key]

#         if arr[0] > timestamp:
#             return ""

#         left, right = 0, len(arr) - 1

#         ans = -1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if arr[mid] <= timestamp:
#                 ans = mid
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return self.info[(key, arr[ans])]

class TimeMap:

    def __init__(self):
        self.info = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.info:
            self.info[key] = []

        self.info[key].append((timestamp, value))

    def get(self, key:str, timestamp: int) -> str:
        if key not in self.info:
            return ""

        arr = self.info[key]

        left, right = 0, len(arr) - 1
        ans = ""
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= timestamp:
                ans = self.info[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return ans

