scores = [30,60,120,80,100]

print("Highest =", max(scores))
print("Lowest =", min(scores))
print("Total =", sum(scores))
print("Average =", sum(scores)/len(scores))

century = 0
half = 0

for i in scores:
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1

print("Centuries =", century)
print("Half-centuries =", half)
