reply=int(input("Enter the number: "))
sum=0

for a in range(2,reply):
    for b in range(2,int((a**0.5)+1)):
        if a%b==0:
            break
    else:
        
        sum+=a
            
        
print("sum of all the primes below given number =",sum)
