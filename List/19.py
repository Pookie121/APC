students = ["A", "B", "C"]

print("Total =", len(students))

name = input("Search student: ")

if name in students:
    print("Present")

students.append("D")
students.remove("C")

print(students)
