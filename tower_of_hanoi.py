#Tower of Hanoi:
def toh(n,source,dest,aux):
    if n==1:
        print(f"{n} moved from {source} to {dest}")
        return
    toh(n-1,source,aux,dest)
    print(f"{n} moved from {source} to {dest}")
    toh(n-1,aux,dest,source)
source,aux,dest="A","B","C"
n=3
toh(n,source,dest,aux)
