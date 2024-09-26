import random

# making a random product list 
Q = ["A" , "C" , "B" , "R"]
Pr = random.choices(Q, k=20)
Pr.append("*")

#for test if loop stops after "*" the last R doesn't count
Pr.append("R")

print( "this is your product list \n \n" + str(Pr) + "\n " )



R = 0
for i in Pr:
    if i == "R" :
        R += 1
    elif i == "*" :
        print("counting is over")
        break

print(str(R)+ " products are rejected")
  


