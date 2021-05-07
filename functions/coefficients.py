def funct():
    a=int(input("enter the first coefficient i.e coefficient of x**2: "))
    b=int(input("enter the second coefficient i.e coefficient of x: "))
    c=int(input("enter the third coefficient: "))
    D=b**2-(4*a*c)
    return D
determinant=funct()
print(determinant)
