reply=int(input("Up To Which Number You Need = "))
tot=0
for i in range(2,reply):
    for j in range(2,i):
        if i%j==0:
            break

    else:
        tot=tot+i


print("Total Value Of The Needed Prime Numbers = ",tot)
