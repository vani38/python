x=20
def number():
    x=50
    print(x)
number()
print(x)


#global x value
x=20
def number():
    global x
    x=50
    print(x)
number()
print(x)
