
#Stack using list:
stack=[]
def push(data):
    stack.append(data)
def pop():
    return stack.pop()
def display():
    return stack
while True:
    c=int(input("Enter choice 1-push() 2-pop() 3-display() 4-exit"))
    if c==1:
        push(int(input("Enter push data: ")))
    elif c==2:
        print(pop(),"is poped")
    elif c==3:
        print(display())
    else:
        break





