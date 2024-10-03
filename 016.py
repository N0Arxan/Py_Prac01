Temp = int(input("enter a Temp"))
M = 0
P = 0
while Temp != 0 :
    if Temp < 0 :
        M += 1
    else :
        P+= 1
    Temp = int(input())

print( M , "negetive Temps \n" , P ,"positive Temps")
