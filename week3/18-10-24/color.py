a = []
n = int(input("Enter the number of colours: "))
for i in range(n):
    colours = input("Enter a colour: ")
    a.append(colours)
print(a)
print("First colour:", a[0])
print("Last colour:", a[-1])
