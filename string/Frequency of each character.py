s = input("Enter string: ")

for i in s:
    if s.index(i) == s.find(i):
        print(i, "=", s.count(i))
