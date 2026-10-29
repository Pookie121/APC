s = input("Enter sentence: ")
words = s.split()
print("Shortest word =", min(words, key=len))
