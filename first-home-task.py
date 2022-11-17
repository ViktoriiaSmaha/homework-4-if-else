a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

if a > 10 and b > 10 and c > 10:
    if a % 3 == 0 and b % 3 == 0:
        print("yes")
    else:
        print("no")
else:
    print("no")
print("end")