class Stack:
    def __init__(self):
        self.places = []

    def push(self, place):
        self.places.append(place)

    def pop(self):
        if not self.is_empty():
            return self.places.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.places[-1]
        else:
            return None

    def is_empty(self):
        return len(self.places) == 0

    def size(self):
        return len(self.places)


# Example usage:
travel_stack = Stack()

travel_stack.push("Home")
travel_stack.push("Terminal")
travel_stack.push("University")
travel_stack.push("Library")
travel_stack.push("Public Market")

print("Places visited (in reverse order of arrival):")
while not travel_stack.is_empty():
    location = travel_stack.pop()
    print(f"- {location}")

print("\nReturning home...") #Illustrates going back to the origin