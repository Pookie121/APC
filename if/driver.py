m = input("Are you married? (yes/no): ").lower()
s = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

if m == "yes" or (s == "male" and age > 30) or (s == "female" and age > 25):
    print("Driver is insured")
else:
    print("Driver is not insured")
