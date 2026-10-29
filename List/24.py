nums = [1,2,3,4,5]

left = nums[1:] + nums[:1]
right = nums[-1:] + nums[:-1]

print("Left:", left)
print("Right:", right)
