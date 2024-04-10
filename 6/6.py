sum=0
sum_of_squares=0
for i in range(1,101):
    sum+=i
    sum_of_squares+=(i**2)

print("Sum Of The Squares=",sum_of_squares)

print("The Square Of The Sum Of Numbers=",(sum*sum))


print("Difference=",(sum*sum)-sum_of_squares)
    
    
