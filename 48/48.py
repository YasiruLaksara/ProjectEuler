sum=0
for a in range (1,1001):
    term=a**a
    sum+=term
print("Sum of the series : ",sum)
reverse_digits=str(sum)[-1:-11:-1]
print("Last Ten Digits : ",reverse_digits[::-1])
