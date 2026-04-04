
# #basic closure:
def outer():
    def inner():
        print("Hi")
    inner()
outer()

#counter colsure:
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        return count
    return inner
c=outer()
print(c());print(c())

#fuction factory:
def multipiler(n):
    def multiply(x):
        return x*n
    return multiply
double=multipiler(2)
triple=multipiler(3)
print(double(5))
print(triple(5))

# #Add prefix:
def prefix(pre):
    def message(msg):
        return pre+msg
    return message
str=prefix("un")
print(str("possible"))
str2=prefix("un")
print(str2("do"))

#use nonlocal to modify:
def original(data):
    def modified(mod):
        nonlocal data
        data=mod
        return data
    return modified
str=original("this")
print(str("that"))
str2=original("then")
print(str2("now"))

#closure Accumulator:
def accumulator():
    total=0
    def sum(data):
        nonlocal total
        total+=data
        return total
    return sum
add=accumulator()
print(add(5))
print(add(3))
print(add(7))
print(add(12))

#password checker:
def password(data):
    pas=data
    def checker(s):
        if pas==s:
            return "Access granted. "
        return "Access Denied. "
    return checker
s=input("Register password: ")
ans=input("Enter password: ")
check=password(s)
print(check(ans))

#fuction logger:
def logger(func):
    def log(*args):
        print(f"Function {func.__name__} is called with {args}")
        return func(args[0],args[1]) 
    return log
def exe(a,b):
    return a+b
add=logger(exe)
print(add(5,6))
print(add(5,6))

#State-full Function:
def function():
    count=0
    def subfunction():
        nonlocal count
        count+=1
        return count
    return subfunction
counter=function()
print(f"function is called for {counter()} times.")
print(f"function is called for {counter()} times.")
print(f"function is called for {counter()} times.")

# #Discount Calculator:
def discount(n):
    def calculate(x):
        return x-((x/100)*n)
    return calculate
price=discount(20)
print(price(54))
print(price(150))
print(price(200))
  
#add prefix n suffix:
def concate(pre,suf):
    def message(msg):
        return pre+msg+suf
    return message
str=concate("My "," Anand")
print(str("name is"))

#counter with reset:
def function():
    count=0
    def counter(action="continue"):
        nonlocal count
        if action=="reset":
            count=0
            return f"reset to {count}"
        count+=1
        return count
    return counter
c=function()
print(c())
print(c())
print(c("reset"))
print(c())

#running average:
def average():
    counter=0
    sum=0
    def running(n):
        nonlocal counter
        nonlocal sum
        sum+=n
        counter+=1
        return sum/counter
    return running
avg=average()
print(avg(5))
print(avg(10))
print(avg(10))

#Bank balance tracker:
def bank(amount):
    def tracker(n):
        nonlocal amount
        amount+=n
        return amount
    return tracker
balance=bank(10000)
print("Balance: ₹",balance(500))
print("Balance: ₹",balance(-5000))
print("Balance: ₹",balance(200))
print("Balance: ₹",balance(-760))

#toggle function:
def function(state):
    def toggle():
        nonlocal state
        state=not state
        return state
    return toggle
tog=function(True)
print(tog())
print(tog())
print(tog())
print(tog())

#generate unique id:
def generate(n):
    def unique():
        nonlocal n
        n+=1
        return n
    return unique
id=generate(19000)
print(f"ID: {id()}")
print(f"ID: {id()}")
print(f"ID: {id()}")
print(f"ID: {id()}")

# #password eval:
def set_password(password):
    count=0
    def check(data):
        nonlocal password
        nonlocal count
        if count>=3:
            return "Access Denied. "
        count+=1
        return "Success. " if password==data else f"Worng password. Attempts left {3-count}."
    return check
check=set_password(input("Register password: "))
while True:
    ans=check(input("Enter password: "))
    print(ans)
    if ans=="Access Denied. ":
        break
    if ans=="Success. ":
        break
    a=input("Press Enter to continue or 4 to stop: ")
    if a=="4":
        break











    
    
    
    
    
    
    





































































