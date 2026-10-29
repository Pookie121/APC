s = input("Enter string: ")
chars = sorted(set(s), key=s.count, reverse=True)

if len(chars) >= 2:
    print("Second most frequent:", chars[1])
else:
    print("No second character")
