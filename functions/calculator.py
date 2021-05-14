from math import sin, cos, log10, radians
print("What would you like to do?")
print("1. Log10(x)")
print("2. Sin(x)")
print("3. Cos(x)")

n = int(input("Enter your choice(1-3): "))

x = int(input("Enter value of x : "))
if n == 1:
    print("Log of",(x),"with base 10 is",log10(x))
elif n == 2:
    print("Sin(x) is ",sin(radians(x)))
elif n == 3:
    print("Cos(x) is ",cos(radians(x)))
else:
    print("Invalid Choice")
