a=input("enter the  text:")
b=input("enter the word")
c=[]
count=0
s=a.split(" ")
#print(len(b))
#print(len(s))
for i in range(0,len(s)):
    if (b == s[i]):
        count=count+1
print('count of the word is ;',count)
