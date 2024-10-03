years = input("enter secuence of year:Exm 1900,2300,2015 \n").split(',')
years = list(map(int,years))
sig20 = 0
for i in years :
    if 1900 <= i <= 1999 and i % 10 == 0 :
        sig20 +=1

print (sig20)

#years for test : 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010
#output : 10
