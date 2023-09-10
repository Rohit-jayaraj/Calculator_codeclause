def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def mul(x,y):
    return(x*y)

def div(x,y):
    return(x/y)

def rem(x,y):
    return(x%y)

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

print("1.Add\n2.Substract\n3.Multiply\n4.Divide\n5.Remainder\n6.Quit\n")
ch = int(input("Enter choice:"))

if(ch==1):
    print("Sum is :" , add(a,b))
elif(ch==2):
    print("Difference is :" , sub(a,b))
elif(ch==3):
    print("Product is :" , mul(a,b))
elif(ch==4):
    print("Quotient is :" , div(a,b))
elif(ch==5):
    print("Remainder is :" , rem(a,b))
elif(ch==6):
    exit()
else:
    pritnt("Invalid input")
