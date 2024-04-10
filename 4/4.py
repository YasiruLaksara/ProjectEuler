max=0
for i in range (100,1000,1):
    for j in range(100,1000,1):
        
        product=i*j

        string=str(product)
        
        if (string==string[::-1]):

            if (max<product):
                max=product

        else:
            continue

print("The Largest Palindromic Number= ",max)






            

            
            

          
