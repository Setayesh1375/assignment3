adad1 = int(input("please enter your first Number: "))
adad2 = int(input("please enter your second Number: "))
Bmm = 0

if adad1 > adad2:
    x = adad2

elif adad1 < adad2:
    x = adad1

for i in range(1 , x+1):
    if adad1 % i == 0 and adad2 % i == 0:
        Bmm = i


kmm = int((adad1 * adad2)/Bmm)
print("Kmm = " , kmm) 