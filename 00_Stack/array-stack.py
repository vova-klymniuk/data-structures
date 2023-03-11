from sys import maxsize
# Implementing Stack using Arrays:

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)

    return stack.pop()

def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]

stack = createStack()
push(stack, str(2))
push(stack, str(4))
push(stack, str(8))
print(pop(stack) + " popped from stack")
