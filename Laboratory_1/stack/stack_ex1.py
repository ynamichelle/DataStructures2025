class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage with a name:
name = "Joanna"
stack = Stack()

print("Pushing name onto the stack...")
for char in name:
    stack.push(char)
    print(f"  Stack: {stack.items}")

print("\nPopping name from the stack...")
reversed_name = ""
while not stack.is_empty():
    char = stack.pop()
    reversed_name += char
    print(f"  Stack: {stack.items}, Popped: {char}, Reversed: {reversed_name}")

print(f"\nOriginal name: {name}")
print(f"Reversed name (from stack): {reversed_name}")