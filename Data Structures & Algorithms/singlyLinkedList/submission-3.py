class LinkedList:
    
    def __init__(self):
        self.store = []
    
    def get(self, index: int) -> int:
        if index >= len(self.store):
            return -1
        return self.store[index]

    def insertHead(self, val: int) -> None:
        self.store.append(None)
        
        # for i in range(1, len(self.store)):
        #     self.store[i] = self.store[i-1]

        for i in range(len(self.store) - 1, 0, -1):
            self.store[i] = self.store[i - 1]

        self.store[0] = val

    def insertTail(self, val: int) -> None:
        self.store.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.store):
            return False

        if index == len(self.store) - 1:
            self.store.pop()
            return True
        
        for i in range(index, len(self.store) - 1):
            self.store[i] = self.store[i+1]

        self.store.pop()
        
        return True
        
    def getValues(self) -> List[int]:
        return self.store
