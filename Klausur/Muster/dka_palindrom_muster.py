from typing import Optional


class Stack:
    def __init__(self):
        self.x = []

    def push(self, item: str) -> None:
        self.x.append(item)

    def peek(self) -> Optional[str]:
        return self.x[-1] if self.x else None

    def pop(self) -> Optional[str]:
        return self.x.pop() if self.x else None


def is_palindrom(w: str) -> bool:
    stack = Stack()
    w = w.lower()

    if len(w) % 2 == 0:
        for index, char in enumerate(w):
            if index < len(w) // 2:
                stack.push(char)
            else:
                if char != stack.peek():
                    return False
                else:
                    stack.pop()
        return True

    else:
        for index, char in enumerate(w):
            if index < len(w) // 2:
                stack.push(char)
            elif index > len(w) // 2:
                if char != stack.peek():
                    return False
                else:
                    stack.pop()
        return True
