import random

# Generate a list of 10 random numbers between 0 and 
nums =[]
i = 0
while i<10 :
    i+=1
    m = random.random ()
    nums.append(m)

print("Random measurements: \n", nums)

num_x = 0
for x in nums :
    if 0.9<x<1 :
        num_x +=1
print("entre 0.9 and 1 : " , num_x)