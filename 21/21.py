reply=int(input("Enter Up To Which Value Do you Need To Find Sum Of Amicable Numbers: "))
num=1
Summation=0
while num<reply:
    tot=0
    sum=0
    list1=[]
    for a in range(1,int(num/2)+1):
        if num%a==0:
            list1.append(a)
            
    for value in list1:
        sum+=value
    
    list2=[]
    for b in range(1,int(sum/2)+1):
        if sum%b==0:

            list2.append(b)

    for val in list2:
        tot+=val

    if sum==tot:
        pass
        
    elif tot==num:
        print(num)
        Summation+=num

    

    num+=1

else:
    
    print("Total Value= ",Summation)
