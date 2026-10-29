marks = [70,80,90,60,50]

highest = max(marks)
lowest = min(marks)
avg = sum(marks)/len(marks)

above = 0
below = 0

for i in marks:
    if i > avg:
        above += 1
    elif i < avg:
        below += 1

print(highest, lowest, avg, above, below)
