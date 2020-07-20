
import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = queue.Queue()
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.put(x)
        for i in range(self.size):
            self.q.put(self.q.get())
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.size -= 1
        return self.q.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        temp = self.q.get()
        self.q.put(temp)
        for i in range(self.size - 1):
            self.q.put(self.q.get())
        return temp
    
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
