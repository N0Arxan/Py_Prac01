y = int(input ("enter your year : "))
if (y%4 == 0 and y%100 != 0) or y%400 == 0 :
    print (str(y) + " is leap year")
else :
    print (str(y) + " is not leap year")
