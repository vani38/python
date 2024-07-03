#collections
#Counter
from collections import Counter
x=Counter(['a','b','c','d','e','c','b','a','d','c','a','b','e','d','f','c'])
print(x)

#Chainmap
from collections import ChainMap
a={'x':10,'y':20}
b={'m':30,'n':40}
c=ChainMap(a,b)
print(c)
print(c['n'])
print(c['x'])

#orderedDict
from collections import OrderedDict
a=OrderedDict()
a['x']=1
a['y']=2
a['z']=3
print(a)

