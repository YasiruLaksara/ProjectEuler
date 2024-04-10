num=1
set1=set()
while num<28123+1:
    total=0
    for a in range(1,int(num/2)+1):
        if num%a==0:
            total+=a

    if total>num:
        set1.add(num)
        
            
            
    num+=1
set2=set()
set3=set()
for k in range(1,28123+1):
    set3.add(k)
    for j in range(1,28123+1):
        if k+j>28123:
            break
        else:
            
            set2.add(k+j)
    


set4=set1 & set2
set5=set2-set4


sum=0
for y in set5:
    sum+=y

print(sum)
