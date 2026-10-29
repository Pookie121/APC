p = input("Enter password: ")

if (len(p) >= 8 and any(i.isupper() for i in p)
    and any(i.islower() for i in p)
    and any(i.isdigit() for i in p)
    and any(not i.isalnum() for i in p)):
    print("Valid password")
else:
    print("Invalid password")
