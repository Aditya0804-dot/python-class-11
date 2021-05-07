def gen(g,n):
    if g=="M":
        print("Hello Mr.",n)
    elif g=="F":
        print("Hello Ms.",n)
    else:
        print("please enter the correct gender form")
gender=input("enter the gender(M/F) of the person in capitals: ")
name=input("enter the name of the person: ")
gen(gender,name)
