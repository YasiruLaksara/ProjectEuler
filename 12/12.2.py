reply=int(input("over how many divisors do you need?"))
flag=True
a=7


while flag:
    
    term=int((a*(a+1))/2)
    

    count=2
       
    while term<=2:
        if term%2==0:
            b=term/2
            
            if term%b==0:
                
                count+=1
                term=term/b
            else:
                b=b-1
                    
                if count>reply:
                    flag=False
                    break
        else:
            b=term
            
            if term%b==0:
                
                count+=1
                term=term/b
            else:
                b=b-1
                    
                if count>reply:
                    flag=False
                    break

        
        
         
            
                    
    else:
        a=a+1
else:
    print((a*(a+1))//2)
    
    

