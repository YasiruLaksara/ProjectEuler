reply=int(input("How Many Divisors You Need Greater = "))
i=0
T=0

flag=True
while flag:
    i=i+1
    T=i*(i+1)/2
    

    
    count=0
    for j in range(1,int(T+1)):
        
        if T%j==0:
            count=count+1
            if count>reply:
               
                flag=False

            else:
                continue

        else:
            continue

print("Triangular Number = ",int(T))
    
        
    

    
