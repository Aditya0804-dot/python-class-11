def calcpow(power,number):
    ans=number**power
    return ans
exponent=int(input("enter an exponential value: "))
base=int(input("enter a base value: "))
answer=calcpow(exponent,base)
print(answer)
