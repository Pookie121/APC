s = input("Enter sentence: ")
words = s.split()
print("Longest word =", max(words, key=len))
