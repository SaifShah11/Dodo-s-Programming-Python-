#0 1 2 3 4 5 6 7 8 9
#  0 1 2 3 4 5 6 7 8
#    0 1 2 3 4 5 6 7

for i in range(0,10): #Rows
    for j in range(i): #Spacing
        print(' ', end=' ')
        
    for k in range(0,10-i): #Printing
        print(k,end=' ')
    print()
      
    


#i=0, j=0,1,2,3,4,5,6,7,8,9 (0,10-0=10)
#i=1, j=0,1,2,3,4,5,6,7,8(0,10-1=9)
    
