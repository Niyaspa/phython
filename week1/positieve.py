li=[]
n=int(input("enter the size of ist"))
for i in range(0,n):
        e=int(input("enter the element of list"))
        li.append(e)

print("positieve numbeer in",li,"are:")
for i in li:
    if i >=0:
        print(i, end=" ")
