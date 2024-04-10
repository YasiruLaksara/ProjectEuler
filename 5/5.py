number=20
flag=True
while flag:
        count=0
        
        for a in range(1,21):
            if number%a==0:
                count=count+1
                if count==20:
                        flag=False                   
                    
            else:
                number+=20
             
    
print("Smallest Positive Number = ",number)
