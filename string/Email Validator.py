e = input("Enter email: ")

if "@" in e and "." in e and e.index("@") < e.rindex(".") and " " not in e:
    print("Valid email")
else:
    print("Invalid email")
