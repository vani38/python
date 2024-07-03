n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def numbers(n):
    even_numbers=[]
    odd_numbers=[]
    for i in n:
        if (i%2)==0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return even_numbers,odd_numbers

even,odd=numbers(n)

print('even numbers:',even)
print('odd numbers:',odd)
print('even numbers:',len(even))
print('odd numbers:',len(odd))
