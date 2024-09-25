#print ("hello")
a =int( input ("f:") )
b =int( input ("l:") )
#for x in range (int(a) ,int(b)+1):
#    print(x)
while a!=b :
    if a<b :
        b = b-a
    else :
        a = a-b
print ( a )     

