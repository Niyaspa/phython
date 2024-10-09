str=(input("enter a string "))
a=[]
vowels=['A','a','E','e','I','i','O','o','U','u']
for i in str:
    if(i in vowels):
        a.append(i)
print("the vowels are",a)            
