phone_number = input("Telefon raqamingizni kiriting: ")
if phone_number.startswith(("90", "91")):
    print("Beeline")
else:
    if phone_number.startswith(("93", "94")):
        print("Ucell")
    else:
        if phone_number.startswith(("99", "95")):
            print("Uzmobile")
        else:
            if phone_number.startswith(("88", "97")):
                print("Mobiuz")
            else:
                print("Noma'lum")