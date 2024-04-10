reply=int(input("Enter The Number Of Digits That Need TO Contain: "))
pre=1
after=1
count=1
flag=True

while flag:
    pre,after=after,pre+after
    count+=1


    if len(str(pre))==reply:
        print(count)
        break
    

