def stack():
    s = []
    return s
def push(s,data):
    s.append(data)
def pop(s):
    return s.pop()
def peek(s):
    return(s[-1])
def isEmpty(s):
    return s == []
def size(s):
    return len(s)