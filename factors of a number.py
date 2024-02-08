number = float(input("provide a number, and I will determine its factors"))
x = 1
factors = []
while x <= number:
    if number % x == 0:
        factors.append(x)
        x+=1
    else:
        x+=1
print(factors)
