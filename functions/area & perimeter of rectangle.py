def calcAreaPeri(l,b):
    ar=l*b
    peri=2*(l+b)
    return (ar,peri)

length=int(input("enter the length of the rectangle: "))
breadth=int(input("enter the breadth of the rectangle: "))
Area,Perimeter=calcAreaPeri(length,breadth)
print("area of the rectangle is ",Area) 
print("perimeter of rectangle is ",Perimeter)
