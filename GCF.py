number1 = float(input("provide 2 numbers, and I will determine the GREATEST COMMON FACTOR between them"))
number2 = float(input("can i get another one?"))
x = 1
factors1 = []
while x <= number1:
    if number1 % x == 0:
        factors1.append(x)
        x+=1
    else:
        x+=1
        x = 1
factors2 = []
while x <= number2:
    if number2 % x == 0:
        factors2.append(x)
        x+=1
    else:
        x+=1