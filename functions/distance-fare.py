def AssignFare(c,a,d):
    if d<500:
        t_fare=(a*200)+(c*(200/2))
    elif (d<1000) and (d>=500):
        t_fare=(a*300)+(c*(300/2))
    else:
        t_fare=(a*500)+(c*(500/2))
    return t_fare

child=int(input("enter the number of children: "))
adult=int(input("enter the number of adults: "))
distance=float(input("enter he distance travelled: "))
trip_fare=AssignFare(child,adult,distance)
print(trip_fare)
