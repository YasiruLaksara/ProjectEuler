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
    for l in range(1,28123+1):
        summation=0
        Summation=k+l

        if summation>28123:
            break

        else:
            set2.add(summation)


            
set4=set1&set2

set5=set3-set4
sum=0
for y in set5:
    sum+=y
print(sum)









##    
##    set3.add(k)
##    for val in set1:
##        term=k-val
##
##        if term<0:
##            continue
##        else:
##            set2.add(term)
##set4=set()
##
##set4=set1 & set2
##set5=set3-set4
##print(min(set5))
##print(36 in set5)
##sum=0
##for y in set5:
##    sum+=y
##
##print(sum)    
