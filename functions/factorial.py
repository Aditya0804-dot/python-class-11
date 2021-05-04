def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
num=int(input("enter a number: "))
factorial=fact(num)
print(factorial)
