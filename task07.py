email = input("Emailingizni kiriting: ")
idx = email.find("@")
if "@" in email and "." not in email[:idx + 1] and " " not in email:
    print("Email manzili tug'ri")
else: 
    print("Email manzili notug'ri")