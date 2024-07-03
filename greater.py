def source(k):
    if (k>0):
       r=k+source(k-1)
       print(r)
    else:
        r=0
    return r
