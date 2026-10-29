salary = [25000,60000,45000,70000]

print("Highest =", max(salary))
print("Lowest =", min(salary))
print("Average =", sum(salary)/len(salary))

for i in salary:
    if i > 50000:
        print("Above 50000:", i)
    if i < 30000:
        print("Below 30000:", i)
