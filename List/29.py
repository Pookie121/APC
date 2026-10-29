temp = [30,32,35,28,40]

avg = sum(temp)/len(temp)

print("Hottest =", max(temp))
print("Coldest =", min(temp))
print("Average =", avg)

for i in temp:
    if i > avg:
        print("Above Avg:", i)
    elif i < avg:
        print("Below Avg:", i)
