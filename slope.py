x1=int(input("enter the value1:"))
x2=int(input("enter the value2:"))
y1=int(input("enter the value3:"))
y2=int(input("enter the value4:"))
s=(y2-y1)/(x2-x1)
if s>0:
    print("positive slope")
elif s<0:
    print("negative slope")
elif s==0:
    print("horizontal line")
else:
    print("vertical line")

    