deposit_payment = int(input("Omonatingizni kiriting: "))
if deposit_payment < 100000:
    print("5%")
if deposit_payment >=100000 and deposit_payment <=500000:
    print("7%")
if deposit_payment > 500000:
    print("10%")