#evens
n=[1,2,3,4,5,6,7,8,9,10,11,15,27,30,42,68]
evens=filter(lambda x:x%2==0,n)
print(list(evens))

#odds
n=[1,2,3,4,5,6,7,8,9,10,11,23,43,53,65,45,66,78,90,98,99]
odds=filter(lambda x:x%2!=0,n)
print(list(odds))
