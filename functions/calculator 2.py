x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("What would you like to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

n = int(input("Enter your choice:(1-4) "))

if n == 1:
    print("The result of addition:",(x + y))
elif n == 2:
    print("The result of subtraction:",(x - y))
elif n == 3:
    print("The result of multiplication:",(x * y))
elif n == 4:
    print("The result of division:",(x / y))
else:
    print("Invalid Choice")