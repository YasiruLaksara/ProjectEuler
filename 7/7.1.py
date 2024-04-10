reply=int(input("Enter What Term Is Needed: "))
count=0
a=1
while count<reply:
    a=a+1

    for b in range(2,(int(a**(0.5))+1)):
        if a%b==0:
            break
    
    else:
        
        count+=1

else:
    print(a)
    
