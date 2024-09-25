
time = input('Enter a time h,m,s \n').split(',')

h,m,s = map(int, time)
if h < 24 or m > 60 or s > 60 or h < 24 or m < 0 or s < 0 :
    print("the time format is incorrect")
else:
    s += 1
    print(str(h)+":"+str(m)+":"+str(s))

