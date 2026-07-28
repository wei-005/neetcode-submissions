# class LinkedList:
    
#     def __init__(self):
#         self.store = []
    
#     def get(self, index: int) -> int:
#         if index >= len(self.store):
#             return -1
#         return self.store[index]

#     def insertHead(self, val: int) -> None:
#         self.store.append(None)
        
#         # for i in range(1, len(self.store)):
#         #     self.store[i] = self.store[i-1]

#         for i in range(len(self.store) - 1, 0, -1):
#             self.store[i] = self.store[i - 1]

#         self.store[0] = val

#     def insertTail(self, val: int) -> None:
#         self.store.append(val)

#     def remove(self, index: int) -> bool:
#         if index >= len(self.store):
#             return False

#         if index == len(self.store) - 1:
#             self.store.pop()
#             return True
        
#         for i in range(index, len(self.store) - 1):
#             self.store[i] = self.store[i+1]

#         self.store.pop()
        
#         return True
        
#     def getValues(self) -> List[int]:
#         return self.store
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
       self.tail.next = ListNode(val)
       self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        
    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

