def discriminant():
    a=int(input("enter the first coefficient i.e coefficient of x**2: "))
    b=int(input("enter the second coefficient i.e coefficient of x: "))
    c=int(input("enter the third coefficient: "))
    D=b**2-(4*a*c)
    return D
disc=discriminant()
if(disc > 0 ):
    print("The quadratic equation has two real roots.")
elif(disc == 0 ):
    print("The quadratic equation  has one real root.")
else:
    print("The quadratic equation  doesn't have  any real root.")

