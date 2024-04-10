number=600851475143
a=2
largestprime=0

while number>1:
    if number%a==0:
        number/=a
        print(number)
        if largestprime<a:
            largestprime=a
    else:
        a=a+1

print("The Largest Prime Factor = ",largestprime)            
        

