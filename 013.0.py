import random

#this is a mistake answer i got the question bad but it was intersting idont remove it


# making a random product list 

Q = ["A" , "C" , "B" , "R"]
Pr = random.choices(Q, k=20)
Pr.append("*")
print( "this is your product list \n \n" + str(Pr) + "\n " )

AA = 0
# intersting mistake with this loop index(i) it always returns the number of first A in the Arrey

#for i in Pr:
#    if i == "A" and Pr[Pr.index(i) + 1] == "A"  :
#        print(Pr[Pr.index(i) + 1])
#    elif i == "*" :
#        print("counting is over")
#        break
#
#print(str(AA)+ " products are AA contuinsly")

#correction :

for i in range(len(Pr)-1): 

    if Pr[i] == "A" and Pr[i + 1] == "A":
        AA += 1

    elif Pr[i] == "*":
        print("Counting is over")
        break

print(str(AA) + " products are AA continuously")



  







