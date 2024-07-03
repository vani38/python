class calculator:
    def operate(self,*args):
        if len(args)==1:
            return args[0]**2
        elif len(args)==2:
            return args[0]+args[1]
        elif len(args)==3:
            return args[0]*args[1]*args[0]
        else:
            return "invalid number of arguments"
calc=calculator()
print(calc.operate(2))
print(calc.operate(2,3))
print(calc.operate(2,3,4))
print(calc.operate(2,3,4,5))
