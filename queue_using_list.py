#Queue using list:
queue=[]
def enqueue(data):
    queue.append(data)
def dequeue():
    return queue.pop(0)
def display():
    return queue
while True:
    c=int(input("1-Enqueue 2-Dequeue 3-Display 4-exit: "))
    if c==1:
        enqueue(int(input("Enter the enqueue data: ")))
    elif c==2:
        print(dequeue(),"is dequeued")
    elif c==3:
        print(display())
    else:
        break
    
