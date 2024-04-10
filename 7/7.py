#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?



print(2)
i=2
count=1
while count<=10000:
    i=i+1
    for j in range(2,i):
        if(i%j==0):
           break
    else:
        count=count+1
        print(i)
        

print()        
print("10001st Prime Number=",i)
        
    
