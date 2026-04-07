import os
with open("file.txt",'w') as f:
    f.write("Message")
with open("file.txt",'r') as f:
    content=f.read()
    print(content)
if os.path.exists("file.txt"):
    print(True)
else:
    print(False)
