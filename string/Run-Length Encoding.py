s = input("Enter string: ")
r = ""
c = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        c += 1
    else:
        r += s[i-1] + str(c)
        c = 1

if s:
    r += s[-1] + str(c)

print(r)
