q = input("enter quality : ")
primer = q
num = 0
while q != "*" :
    if q == primer :
        num += 1
    q = input()
print(num)
