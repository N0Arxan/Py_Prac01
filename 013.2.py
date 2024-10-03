Qual= input("Enterar un Qualitat fuera de while: ")
num = 0
seguir = True
while not(Qual  == "*"  or not seguir):

    num += 1

    if Qual == "A":

        Qual1 = input("Enterar otra  :")

        if Qual1 == Qual:
            
            seguir = False
            
    
    if seguir == True:
        Qual = input("Enterar un Qualitat while 1 : ")

print(num-1)



