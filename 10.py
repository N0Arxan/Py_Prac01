x = float(input("enter x : \n"))
if x < 2 :
    x=x/x-2
elif x >= 2 and x <= 5 :
    x=x**2-4
else :
    x=x*2-4
print(x)