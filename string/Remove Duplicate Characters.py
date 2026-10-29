s = input("Enter string: ")
r = ""

for i in s:
    if i not in r:
        r += i

print(r)
