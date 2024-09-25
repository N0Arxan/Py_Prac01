
val = int(input("amount of money :"))

b_500 = val // 500
val = val % 500

b_200 = val // 200
val = val % 200

b_100 = val // 100
val = val % 100

b_50 = val // 50
val = val% 50

b_20 = val // 20
val = val % 20

b_10 =val // 10
val = val % 10

b_5 = val // 5
val = val % 5

m_2 = val // 2
val = val % 2

m_1 = val // 1

print("500 = " + str(b_500))
print("200 = " + str(b_200))
print("100 = " + str(b_100))
print("50 = " + str(b_50))
print("20 = " + str(b_20))
print("10 = " + str(b_10))
print("5 = " + str(b_5))
print("2 = " + str(m_2))
print("1 = " + str(m_1))
