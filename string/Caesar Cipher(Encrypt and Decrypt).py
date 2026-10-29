s = input("Enter message: ")
k = int(input("Enter shift: "))

for i in s:
    if i.isalpha():
        start = ord('A') if i.isupper() else ord('a')
        print(chr((ord(i) - start + k) % 26 + start), end="")
    else:
        print(i, end="")
print()
