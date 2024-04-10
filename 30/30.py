max=(9**5)*5



sum=0
for a in range(2,max+1):
    total=0
    for b in str(a):
        total+=int(str(b))**5


    if total==a:
        sum+=a
        
    
print("Sum Of The Numbers: ",sum)    
