from collections import deque

class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x: int) -> None:
        while len(self.que1) != 0:
            s = self.que1[0]
            self.que2.append(s)
            self.que1.popleft()
        
        self.que1.append(x)

        while len(self.que2) != 0:
            s = self.que2[0]
            self.que1.append(s)
            self.que2.popleft()

    def pop(self) -> int:
        return self.que1.popleft()

    def top(self) -> int:
        return self.que1[0]
        

    def empty(self) -> bool:
        return len(self.que1) == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()