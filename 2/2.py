pre=1
after=2
sum=0
while pre<4000000:
    print(pre, end=' , ')
    
    pre,after=after,pre+after
    
    if (pre%2==0):

        sum=sum+pre
        

print()
print()
print()
print("Sum Of Even Valued Values = ",sum)

    

    
