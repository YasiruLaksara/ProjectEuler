set1=set()
count=0

for a in range(2,101):
    for b in range(2,101):
        value=a**b
        set1.add(value)

print(set1)

print("Number Of Distinct Terms = ",len(set1))
        
