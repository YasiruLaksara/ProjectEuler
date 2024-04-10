def factorial(num):
    if num==1:
        return 1
    else:
        global result  #globalising he variable result
        result=num*factorial(num-1)
        return(result)

factorial(10)

#Method to take sum of digits    
sum=0
for digit in str(result):
    sum+=int(digit)

print("Sum Of The Digits= ",sum)
        

    
    
    
    
