a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

if a > b:
    maximum = a
else:
    maximum = b
if c > maximum:
    maximum = c
print(maximum)
