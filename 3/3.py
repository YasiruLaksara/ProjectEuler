x=600851475143
max=0
for i in range(2,x):
    if x==1:
            break
    while x%i==0:
        x=x/i
        print(i, end=" , ")

        

        if max<i:
            max=i

print()
print()

print("The Largest Prime Factor = ",max)            
    
