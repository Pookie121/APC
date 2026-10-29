patients = ["Ram", "Shyam"]

patients.append("Rita")

name = input("Search patient: ")

if name in patients:
    print("Found")

patients.remove("Shyam")

print(patients)
print("Total Patients =", len(patients))
