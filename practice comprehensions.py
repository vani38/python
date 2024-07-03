#odd numbers
a=[11,23,4,56,7,8,9,10,20,1,32,87,5,24,57]
b=[]
b=[i for i in a if i%2!=0]
print(b)

#even numbers
b={}
b={i:i for i in range(11,30) if i%2==0}
print(b)
