
time = input('Enter a time hh:mm:ss \n').split(':')

h,m,s = map(int, time)

if 0>h>24 or 0>m>60 or 0>s>60  :
    s += 1 
    if s == 60 :
        s = 00
        m += 1
        if m == 60:
            m = 00
            h +=1
            if h == 24:
                h=0
    print(str(h)+":"+str(m)+":"+str(s))

else :
    print("time format is incorrect")

    
    
    
    
    


