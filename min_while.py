numbers=[]
count=0
while count<6:
    number=float(input(f"enter the number{count+1}:"))
    numbers.append(number)
    count+=1
    min_number=min(numbers)
    print("min_num:",min_number)
    
    