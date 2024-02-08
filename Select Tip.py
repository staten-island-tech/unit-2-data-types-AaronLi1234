bill = float(input("what is your bill"))
print("OPTIONS: bad = 1, okay = 2, good = 3, great = 4")
service = float(input("how was your service 1, 2, 3 or 4"))
if service == 1:
    total = float(bill) * 1.00
if service == 2:
    total = float(bill) * 1.15
if service == 3:
    total = float(bill) * 1.20
if service == 4:
    total = float(bill) * 1.25 
print(f"your bill+tip depending on how you rated your service is{total}")
