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
    for val in set1:
        term=k-val

        if term<0:
            continue
        else:
            set2.add(term)
set4=set()

set4=set1 & set2
set5=set3-set4


sum=0
for y in set5:
    sum+=y

print(sum)

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
#print(len(set1^set2))
    



##tot_numbers=0
##def factorial(count):
##    for j in range(1,count+1):
##        tot_numbers*=j
##        
##    return(tot_numbers)
##   
