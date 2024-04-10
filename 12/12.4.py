reply=int(input("over how many divisors do you need?"))
flag=True
a=2


while flag:
    
    term=int((a*(a+1))/2)
    

    count=2
    while term>1:
            
        for b in range(2,int(term+1)):
            if term%b==0:
                
                count+=1
                term=term/b
                                    
                if count>reply:
                    flag=False
                    break
                

                            
                for b in range(2,int(term+1)):
                    if term%b==0:
                
                        count+=1
                        term=term/b

                
                
                
                    
                    if count>reply:
                        flag=False
                        break
                
                    
        else:
            a=a+1
else:
    print((a*(a+1))/2)
    

