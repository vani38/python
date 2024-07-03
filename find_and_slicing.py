#python program to extract a word
a='ram@gmail.com sita@gmail.com'
m=a.find(' ')
print(m)
n=a.find('@',m)
print(n)
print(a[m+1:n])
      
