class shapes:
    def area(self,*args):
        if len(args)==1:
            return 3.14*args[0]**2
        elif len(args)==2:
            return args[0]*args[1]
        else:
            return "invalid number of arguments"
s=shapes()
print(s.area(5))
print(s.area(4,5))
print(s.area(3,4,5))

        
