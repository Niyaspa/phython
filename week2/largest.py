num1=int(input("ENTER THE 1ST NUMBER"))
num2=int(input("ENTER THE SECOND NUMBER"))
num3=int(input("ENTER THE THIRD NUMBER"))

if(num1 >= num2) and (num1 >= num3):
    largest = num1
elif(num2 >= num1) and (num2 >= num3):
    largest =num2
else:
    largest=num3

print("the largest number is",largest)
   
