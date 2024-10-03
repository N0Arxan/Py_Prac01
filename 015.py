# making a random product list 
Pr = ['C', 'R', 'B', 'A', 'C', 'C', 'R', 'R', 'R', 'C', 'R', 'B', 'C', 'C', 'A', 'A', 'R', 'B', 'R', 'R', 'R', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'R']
#nhiha = 2

RBA = 0 
for i in range(len(Pr)-2):
    if Pr[i] == 'R' and Pr[i+1] == 'B' and Pr[i+2] == 'A' :
        RBA +=1 
print(RBA)
