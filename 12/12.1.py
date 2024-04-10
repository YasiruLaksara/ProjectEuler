reply=int(input("over how many divisors do you need?"))
flag=True
a=1


while flag:
    
    term=int((a*(a+1))/2)
    

    count=2
        
    for b in range(2,int(term/2)+1):
        if term%b==0:
            
            count+=1
            
            
                
            if count>reply:
                flag=False
                break
            
                    
    else:
        a=a+1
else:
    print(term)
    
