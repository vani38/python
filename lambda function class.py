y=lambda x:x*x*x
print(y(25))

#list
a=[1,2,3,4,5]
b=[]
c=lambda a:[b.append(i)for i in a]
c(a)
print(b)
