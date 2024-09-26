import random
# making a random product list 
Q = ["A" , "C" , "B" , "R"]
Pr = random.choices(Q, k=20)
print( "this is your product list \n \n" + str(Pr) + "\n " )



num = 0
for i in range(len(Pr)): 
    
    if Pr[i] == "A" and Pr[i + 1] == "A":
        print(str(num) + " products are before AA ")
        break
    else:
        num += 1
else:
    print("no hay AA")

#much easier then i thought :)


