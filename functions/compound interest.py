def compound():
    P=float(input("enter the principal amount: "))
    R=float(input("enter the rate: "))
    T=float(input("enter the total time required: "))
    N=int(input("enter the number of times the interest is compounded: "))
    CI= ((P*(1+R/N))**(N*T))
    return CI
interest=compound()
print(interest) 
