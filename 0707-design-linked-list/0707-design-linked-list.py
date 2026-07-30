class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        curr = self.head
        count = 0

        while curr is not None:
            if count == index:
                return curr.val

            curr = curr.next
            count += 1
        return -1 

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            temp = Node(val)
            self.head = temp
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        temp = Node(val)
        curr.next = temp
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        counter = 0

        if index == 0:
            self.addAtHead(val)
            return 

        while curr is not None:
            if counter == index - 1:
                nxt = curr.next
                temp = Node(val)
                curr.next = temp
                temp.next = nxt
                break 

            curr = curr.next
            counter += 1
                 

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        counter = 0

        if curr is None:
            return
        
        if index == 0:
            self.head = self.head.next
            return

        while curr is not None and curr.next is not None:
            if counter == index - 1:
                curr.next = curr.next.next
                return

            curr = curr.next
            counter += 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)