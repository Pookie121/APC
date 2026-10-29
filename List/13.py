nums = []

for i in range(10):
    nums.append(int(input()))

nums.sort()
print("Ascending:", nums)

nums.sort(reverse=True)
print("Descending:", nums)
