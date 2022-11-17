number = int(input("Enter your number"))

c = number % 10
b = int((number % 100 - c) / 10)
a = int((number - (b * 10 + c)) / 100)


reversed_number = c * 100 + b * 10 + a
print(reversed_number)