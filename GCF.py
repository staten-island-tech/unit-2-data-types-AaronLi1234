number1 = float(input("provide 2 numbers, and I will determine the GREATEST COMMON FACTOR between them"))
number2 = float(input("can i get another one?"))
x = 1
y = 1
factors1 = []
while x <= number1:
    if number1 % x == 0:
        factors1.append(x)
        x+=1
    else:
        x+=1
factors2 = []
while y <= number2:
    if number2 % y == 0:
        factors2.append(y)
        y+=1
    else:
        y+=1
commonfactors = []
for i in factors1:
    if i == i in factors2:
        commonfactors.append(i)
print(commonfactors)
GCF = commonfactors[-1]
print(GCF)


