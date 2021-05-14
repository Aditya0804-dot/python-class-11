def fib(x,y):
    z=x+y
    print(z)
    return y,z

n=int(input("enter the number of terms of fibonacci series to be printed: "))
x=1
y=1
if n<=0:
    print("Please enter positive numbers only")
elif n == 1:
    print(x)
else:
    print(x)
    print(y)
    for i in range(n-2):
        x,y=fib(x,y)
