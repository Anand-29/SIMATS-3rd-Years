#Quick Sort:
def quick(li):
    if len(li)<=1:
        return li
    pivot=li[0]
    left=[x for x in li[1:] if x<=pivot]
    right=[x for x in li[1:] if x>pivot]
    return quick(left) + [pivot] + quick(right)
li=list(map(int,input("Enter the data: ").split()))
ans=quick(li)
print("Sorted list : ",ans)














