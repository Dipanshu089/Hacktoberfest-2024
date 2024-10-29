from collections import deque

def reverse(stack):
    # Base case: if stack is empty, return
    if not stack:
        return

    # Pop the top element
    num = stack.pop()
    # Recursively reverse the rest of the stack
    reverse(stack)
    # Insert the popped element at the bottom
    insert_at_bottom(stack, num)

def insert_at_bottom(stack, x):
    # Base case: if stack is empty, push the element to the bottom
    if not stack:
        stack.append(x)
        return

    # Pop the top element
    num = stack.pop()
    # Recursively insert at the bottom
    insert_at_bottom(stack, x)
    # Push the popped element back on top
    stack.append(num)

# Testing the function
stack = deque([1, 2, 3, 4, 5])
print("Original stack:", list(stack))
reverse(stack)
print("Reversed stack:", list(stack))
