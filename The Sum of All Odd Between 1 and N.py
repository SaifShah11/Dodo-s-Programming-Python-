user=int(input('Enter a Number: '))

z=[]

print()

for i in range(1,user+1):
    if i%2!=0:
        z.append(i)

print(z)

print()

print('The sum of all the odd numbers between 1 to n =', sum(z))
