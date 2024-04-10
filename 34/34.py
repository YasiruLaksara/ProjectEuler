##
##def factorial(n):
##    fact=1
##    while n>0:
##        
##        fact=fact*n
##        n=n-1
##    
##    return
##    
##factorial(5)

a=3
factorial=1
while True:
    list1=[]
    for i in str(a):
        list1.append(int(i))

       
    for k in list1:
        
        total=0  
        for m in range(1,k+1):
            
            factorial*=m

        total+=factorial
