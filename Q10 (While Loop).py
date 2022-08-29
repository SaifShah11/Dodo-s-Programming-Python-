
i=1
while i<=10: #Rows

    for k in range(0,i): #Spacing
        print(' ', end= ' ') 

    j=0
    while j<=10-i: #Printing
        print(j, end=' ')
        j=j+1

    print()
    i=i+1
        

#i=1,k=0(0,1), j=0,1,2,3,4,5,6,7,8,9 (10-1=9)
#i=2,k=0,1 (0,2), j=0,1,2,3,4,5,6,7,8 (10-2=8)

